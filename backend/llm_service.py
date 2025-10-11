import os, json, re, pickle, pdfplumber, faiss, numpy as np
from typing import List, Dict, Any
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
genai.configure(api_key=os.getenv("GOOGLE_AI_API_KEY"))

class Analyzer:
    def __init__(self, model='gemini-2.5-flash'):
        self.model = genai.GenerativeModel(model)
        self.policy_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Public Policies'))
        self.index = None
        self.meta = None
        self._load()

    def _load(self):
        try:
            emb_dir = os.path.join(os.path.dirname(__file__), 'embeddings_storage')
            idx_path = os.path.join(emb_dir, 'combined_policy_index.index')
            meta_path = os.path.join(emb_dir, 'combined_metadata.pkl')
            
            if os.path.exists(idx_path) and os.path.exists(meta_path):
                self.index = faiss.read_index(idx_path)
                with open(meta_path, 'rb') as f:
                    self.meta = pickle.load(f)
        except:
            pass

    async def _search(self, query: str, k: int = 10) -> List[str]:
        if not self.index or not self.meta:
            return []
        
        try:
            result = genai.embed_content(
                model="models/text-embedding-004",
                content=query,
                task_type="RETRIEVAL_QUERY"
            )
            emb = np.array([result['embedding']]).astype('float32')
            _, indices = self.index.search(emb, k)
            
            chunks = []
            for idx in indices[0]:
                if idx < len(self.meta['chunks']):
                    chunks.append(self.meta['chunks'][idx])
            return chunks
        except:
            return []

    def extract_questions(self, path: str) -> List[str]:
        questions = []
        try:
            with pdfplumber.open(path) as pdf:
                text = "".join(page.extract_text() or "" for page in pdf.pages)
                text = re.sub(r'Rev\.\s+\d{2}/\d{4}', '', text)
                text = re.sub(r'Page\s+\d+\s+of\s+\d+', '', text)
                text = re.sub(r'\(Reference:.*?\)', '', text)
                text = text.replace("Yes No Citation:", "").strip()
                splits = re.split(r'\n(?=\d+\.\s)', text)
                
                for s in splits:
                    q = " ".join(s.strip().split())
                    if q and re.match(r'^\d+\.', q):
                        q = re.sub(r'\s*Yes\s*No\s*Citation:\s*$', '', q)
                        questions.append(q)
        except:
            pass
        return questions

    async def analyze_question(self, question: str, all_relevant_docs: List[str], ws):
        await ws.send_json({"type": "status", "message": "Finding relevant sections..."})
        chunks = await self._search(question, k=25)

        if not chunks:
            await self._error(ws, question, "No relevant sections found.")
            return

        await ws.send_json({"type": "status", "message": f"Analyzing {len(chunks)} sections..."})
        context = "\n\n".join([f"Section {i+1}: {c}" for i, c in enumerate(chunks)])
        result = await self._analyze_context(question, context)
        
        await ws.send_json({
            "type": "result",
            "data": {
                "question": question,
                "documents": [],
                "compliance_status": result.get('compliance_status', 'Error'),
                "confidence": result.get('confidence', 0.0),
                "explanation": result.get('explanation', 'Analysis incomplete.'),
                "relevant_sections": result.get('relevant_sections', [])
            }
        })

    async def _analyze_context(self, question: str, context: str) -> Dict[str, Any]:
        prompt = f"""You are a senior healthcare compliance auditor. Analyze if the policy answers the audit question.

        **Step 0: Validate the Question Integrity**
        First, read the user's question. Does it refer to a specific list, chart, or set of items that are not provided in the prompt (e.g., "the five listed services," "as shown in the chart below")?
        - If YES, you must stop. Your final answer **must be "Uncertain,"** and your explanation must state that the question is unanswerable because it contains a missing reference.
        - If NO, proceed with the following steps.

        **Step 1: Deconstruct the Question and Identify its Structure**
        Break the question into all its verifiable claims. Then, determine the question's structure:
        - **Structure A (Factual List):** Is the question a list of factual assertions where all must be true for the statement to be correct? (e.g., "Does the policy state A, B, and C?")
        - **Structure B (Primary/Secondary):** Is there a clear primary claim that is qualified by a conditional, supporting, or minor parenthetical clause? (e.g., "While X is true, does Y happen?" or "Does the policy cover X (including the minor detail Y)?")
        - **Structure C (Core Question with Assumed Context):** Is the prompt composed of a distinct "Core Question" followed by "supporting assertions" that should be assumed to be true and NOT verified?

        **Step 2: Evidence Analysis**
        - Scan all text chunks for direct quotes or strongly implied evidence for the claims you must verify (based on the structure from Step 1).
        - **Apply Semantic Equivalents:** Policy documents use specific language with functional meanings. Apply these equivalents during your analysis:
            - "Shall be responsible for providing" **is equivalent to** "is required to provide."
            - "Shall not be approved for payment" **implies** "the provider is financially liable."
            - A required "Notification" or "Validation" process **is a form of** "authorization."
            - A "new election" process **implies** the same process applies to a "re-election."
        - **Reconcile Apparent Contradictions:** If chunks seem to conflict, analyze the context to find the unifying rule.

        **Step 3: Final Judgment based on Structure**
        Synthesize your findings using the structure identified in Step 1:
        - **If Structure A (Factual List):** You must find support for **ALL verifiable claims** to answer **"Yes"**. If any single claim is contradicted or is not supported by the text, the answer is **"No"**.
        - **If Structure B (Primary/Secondary):** Base your "Yes" or "No" answer on the validity of the **primary claim**. In your explanation, you must still address the secondary clauses.
        **- If Structure C (Core Question with Assumed Context): Base your "Yes" or "No" answer *only* on the evidence for the Core Question. Do NOT verify the supporting assertions and ignore any discrepancies found within them.**
        - Answer **"Uncertain"** only if there is absolutely no information to support or contradict the core of the question.

        Formulate your final answer as a JSON object. Do not add any commentary outside the JSON.

        ---
        **Audit Task:**

        **User Question:** "{question}"

        **Provided Documents:** {context}
        ---

        Return **only** the final JSON object in the specified format:
        {{
        "compliance_status": "Yes", "No", or "Uncertain",
        "confidence": float (0.0-1.0),
        "explanation": "Provide a concise (max 50 words) reasoning for your answer. **Do not restate the question or include direct quotes.** Briefly summarize how the evidence supports your conclusion based on the logic for that structure.",
        "relevant_sections": ["Array of direct quotes or text excerpts that support your conclusion."]
        }}"""

        resp = await self._call(prompt, json=True)
        try:
            return json.loads(resp)
        except:
            return {"compliance_status": "Error", "explanation": "Parse error."}

    async def _call(self, prompt: str, json: bool = False) -> str | None:
        try:
            config = {"max_output_tokens": 8192}
            if json:
                config["response_mime_type"] = "application/json"
            
            resp = await self.model.generate_content_async(
                prompt,
                generation_config=genai.types.GenerationConfig(**config),
            )
            if not resp.parts:
                return None
            return resp.text
        except:
            return None
            
    async def _error(self, ws, question: str, msg: str):
        await ws.send_json({
            "type": "result",
            "data": {
                "question": question,
                "documents": [],
                "compliance_status": "Error",
                "confidence": 0.0,
                "explanation": msg,
                "relevant_sections": []
            }
        })

analyzer = Analyzer()
