"""
LLM Service for Healthcare Policy Compliance Analysis using Google Gemini
"""

import os
import json
import re
from typing import List, Dict, Any
import google.generativeai as genai
from dotenv import load_dotenv
from docs import DOCUMENTS
import pdfplumber

def get_policy_path():
    """Determines the correct path to the 'Public Policies' directory."""
    # In the Docker container, the path is absolute from the root
    docker_path = '/app/Public Policies'
    if os.path.exists(docker_path):
        return docker_path
    # For local development, it's relative to this file
    local_path = os.path.join(os.path.dirname(__file__), '..', 'Public Policies')
    return local_path

POLICY_DIR = get_policy_path()

def configure_genai():
    """Loads the Google AI API key and configures the genai module."""
    # Load from parent directory where .env actually exists
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
    api_key = os.getenv("GOOGLE_AI_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_AI_API_KEY not found in environment variables.")
    genai.configure(api_key=api_key)

class ComplianceAnalyzer:
    """Handles all interactions with the backend generative AI model."""
    def __init__(self):
        """Initializes the compliance analyzer and the generative model."""
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.ALL_POLICY_DOCUMENTS = DOCUMENTS

    async def _call_gemini_api(self, prompt: str, max_tokens: int = 8192) -> str:
        """
        Sends a prompt to the Gemini API and handles potential errors.

        Returns:
            The text response from the model or an error message.
        """
        try:
            response = await self.model.generate_content_async(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=max_tokens
                )
            )
            return self._extract_text_from_response(response)
        except Exception as e:
            print(f"   ❌ Gemini API Error: {e}")
            return f"API Error: {e}"

    def _extract_text_from_response(self, response) -> str:
        """
        Extracts text from a GenerateContentResponse, handling simple and multi-part responses.
        This is necessary because the Gemini API can return responses in different formats.
        """
        try:
            return response.text
        except ValueError:
            try:
                return "".join(part.text for part in response.parts)
            except (AttributeError, TypeError):
                if hasattr(response, 'candidates') and response.candidates:
                    candidate = response.candidates[0]
                    if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                        return "".join(part.text for part in candidate.content.parts)
                return ""
        except Exception as e:
            print(f"   ❌ Unexpected error during text extraction: {e}")
            return ""

    def _extract_document_content(self, filename: str) -> str:
        """
        Finds the specified PDF file within the 'Public Policies' directory
        and extracts its full text content.
        """
        for root, _, files in os.walk(POLICY_DIR):
            if filename in files:
                pdf_path = os.path.join(root, filename)
                try:
                    with pdfplumber.open(pdf_path) as pdf:
                        full_text = " ".join(page.extract_text() for page in pdf.pages if page.extract_text())
                        full_text = re.sub(r'Page\s+\d+\s+of\s+\d+', '', full_text)
                        full_text = re.sub(r'\s+', ' ', full_text).strip()
                        return full_text
                except Exception as e:
                    print(f"   ❌ Error processing PDF {pdf_path}: {e}")
                    return f"Error: Could not read content from {filename}"
        
        print(f"   ❌ Document not found: {filename} in {POLICY_DIR}")
        return f"Error: Document not found - {filename}"

    async def find_relevant_documents(self, question: str) -> List[str]:
        """
        Uses the LLM to find the most relevant document filenames for a single question.
        Now includes descriptions for better accuracy.
        """
        doc_list_str = "\n".join([
            f"- {doc['filename']}: {doc['title']}\n  Description: {doc.get('description', 'No description available')}"
            for doc in self.ALL_POLICY_DOCUMENTS
        ])

        prompt = f"""You are a healthcare policy expert. Your task is to analyze a single audit question and identify the top 2 most relevant policy documents from the master list below.

    Each document includes its filename, title, and a brief description. Use both the title and description to determine relevance.

    Return **only a single, raw JSON object** with one key "documents" containing an array of the top 2 most relevant filenames, sorted from most to least relevant.

    If no documents seem relevant, return an empty array.

    Audit Question:
    "{question}"

    Master list of policy documents:
    {doc_list_str}

    Respond with only the JSON object."""

        response = await self._call_gemini_api(prompt, max_tokens=2048)  # Increased for longer prompt

        try:
            if "API Error" in response or "Error:" in response:
                raise json.JSONDecodeError(f"Received an API error during matching: {response}", response, 0)

            cleaned_response = response.strip().replace('```json', '').replace('```', '').strip()
            result = json.loads(cleaned_response)
            
            docs = result.get("documents", [])
            if isinstance(docs, list) and all(isinstance(d, str) for d in docs):
                return docs
            else:
                print(f"   ⚠️ Unexpected format in matching response: {result}")
                return []
        
        except (json.JSONDecodeError, ValueError) as e:
            print(f"   ❌ Critical failure in document matching step. Error: {e}. Response: {response[:200]}")
            return []

    async def _analyze_single_pass(self, question: str, documents_to_analyze: List[str]) -> Dict[str, Any]:
        """
        Performs a single analysis pass on a question with a given set of documents.
        This is the core analysis function that generates the compliance result.
        """
        if not documents_to_analyze:
            return {
                "compliance_status": "Unable to determine",
                "confidence": 0.0,
                "explanation": "No relevant documents were provided for analysis.",
                "relevant_sections": []
            }

        doc_contexts = []
        for doc_filename in documents_to_analyze:
            content = self._extract_document_content(doc_filename)
            if not content.startswith("Error"):
                doc_contexts.append(f"--- START OF DOCUMENT: {doc_filename} ---\n{content}\n--- END OF DOCUMENT: {doc_filename} ---")

        if not doc_contexts:
            return {
                "compliance_status": "Error",
                "confidence": 0.0,
                "explanation": "Relevant documents were identified, but their content could not be read.",
                "relevant_sections": []
            }

        context = "\n\n".join(doc_contexts)[:50000]

        analysis_prompt = f"""You are a healthcare compliance auditor. Your task is to determine if the provided policy documents contain explicit information that directly answers the audit question.

IMPORTANT: Look for direct evidence in the policy text. If the policy explicitly states responsibilities, requirements, or processes that demonstrate the answer to the question, consider it explicit evidence.

Provide your analysis as a single JSON object with the following keys:
- "compliance_status": (string) Must be "Yes", "No", or "Uncertain".
- "confidence": (float) A score from 0.0 to 1.0. A "Yes" or "No" status requires direct evidence and should have high confidence (> 0.9).
- "explanation": (string) A detailed explanation of your reasoning, **not to exceed 100 words**. Reference specific text from the policy that supports your answer. If the policy lacks relevant information, state this clearly.
- "relevant_sections": (array of strings) Extract the **top 5 most relevant and concise quotes** from the policy that provide evidence for your answer.

**Audit Question:** "{question}"

**Policy Documents Context:**
{context}

Return only the JSON object, with no other text or markdown formatting."""

        llm_response = await self._call_gemini_api(analysis_prompt, max_tokens=8192)

        try:
            cleaned_response = llm_response.strip().replace('```json', '').replace('```', '').strip()
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            return {
                "compliance_status": "Error",
                "confidence": 0.0,
                "explanation": f"The AI model failed to provide a valid analysis. Raw response: {llm_response}",
                "relevant_sections": []
            }

    async def analyze_question(self, question: str, relevant_docs: List[str], websocket):
        """
        Analyzes a question by first checking the single most relevant document.
        If the result is uncertain, it performs a second, combined analysis with the top two documents.
        """
        from fastapi import WebSocket
        if not relevant_docs:
            await websocket.send_json({
                "type": "result",
                "data": {
                    "question": question,
                    "documents": [],
                    "explanation": "No relevant policy documents were identified for this question.",
                    "compliance_status": "Unable to determine",
                    "confidence": 0.0,
                    "relevant_sections": []
                }
            })
            return

        top_document = relevant_docs[0]
        await websocket.send_json({"type": "status", "message": f"Analyzing top document: {top_document.split('/')[-1]}"})
        
        first_pass_analysis = await self._analyze_single_pass(question, [top_document])
        
        status = first_pass_analysis.get('compliance_status')
        confidence = first_pass_analysis.get('confidence', 0.0)

        if status != "Uncertain" and confidence > 0.9:
            final_result = {
                'question': question,
                'documents': [top_document],
                'compliance_status': status,
                'confidence': confidence,
                'explanation': first_pass_analysis.get('explanation', ''),
                'relevant_sections': first_pass_analysis.get('relevant_sections', [])
            }
            await websocket.send_json({"type": "result", "data": final_result})
            return

        if len(relevant_docs) > 1:
            top_two_documents = relevant_docs[:2]
            await websocket.send_json({"type": "status", "message": f"First result uncertain. Re-analyzing with top 2 documents..."})
            
            second_pass_analysis = await self._analyze_single_pass(question, top_two_documents)
            
            final_result = {
                'question': question,
                'documents': top_two_documents,
                'compliance_status': second_pass_analysis.get('compliance_status', 'Uncertain'),
                'confidence': second_pass_analysis.get('confidence', 0.0),
                'explanation': second_pass_analysis.get('explanation', 'No explanation provided.'),
                'relevant_sections': second_pass_analysis.get('relevant_sections', [])
            }
            await websocket.send_json({"type": "result", "data": final_result})
        else:
            final_result = {
                'question': question,
                'documents': [top_document],
                'compliance_status': status,
                'confidence': confidence,
                'explanation': first_pass_analysis.get('explanation', 'No explanation provided.'),
                'relevant_sections': first_pass_analysis.get('relevant_sections', [])
            }
            await websocket.send_json({"type": "result", "data": final_result})

configure_genai()
analyzer = ComplianceAnalyzer()