import os
import tempfile
import traceback
import re

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber

from backend.llm_service import analyzer

# --- FastAPI App Initialization ---

app = FastAPI(
    title="Healthcare Policy Compliance Auditor API",
    description="An API that uses AI to audit healthcare policy documents for compliance.",
    version="1.0.0",
)

# Configure CORS to allow the frontend to communicate with this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://*.vercel.app", "*"], # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Business Logic ---

def extract_questions_from_pdf(pdf_path: str) -> list[str]:
    """
    Extracts and cleans audit questions from a given PDF file.

    This function is designed to parse PDFs that contain lists of questions,
    filtering out common headers, footers, and other non-question text.
    """
    questions = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    # Split the page text into lines and clean them up.
                    lines = [line.strip() for line in text.split('\n')]

                    current_question = ""
                    for line in lines:
                        # Heuristics to identify and filter out non-question lines.
                        is_footer = "Rev." in line or "Page" in line
                        is_header = "Attachment" in line
                        is_instruction = "Yes No Citation:" in line or "(Reference:" in line

                        if line and not is_footer and not is_header and not is_instruction:
                            # If a line starts with a number, it's likely a new question.
                            if re.match(r"^\d+\.", line):
                                if current_question:
                                    questions.append(current_question.strip())
                                current_question = line
                            elif current_question:
                                # Append multi-line questions.
                                current_question += " " + line

                    if current_question:
                        questions.append(current_question.strip())

    except Exception as e:
        print(f"❌ Error processing question PDF: {e}")
        # Return an empty list on failure.
        return []

    return questions

# --- API Endpoints ---

@app.get("/")
def read_root():
    """Health check endpoint to confirm the API is running."""
    return {
        "status": "online",
        "message": "Healthcare Policy Compliance Auditor API is ready for analysis."
    }

@app.websocket("/ws/audit")
async def websocket_audit(websocket: WebSocket):
    """
    WebSocket endpoint to handle the entire audit process in real-time.
    1. Receives a PDF file.
    2. Extracts questions.
    3. Finds relevant policy documents for each question.
    4. Analyzes compliance for each question.
    5. Streams status and results back to the client.
    """
    await websocket.accept()
    temp_file_path = None
    try:
        file_data = await websocket.receive_bytes()

        # Use a temporary file to store the uploaded PDF.
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            temp_file.write(file_data)
            temp_file_path = temp_file.name

        questions = extract_questions_from_pdf(temp_file_path)
        if not questions:
            await websocket.send_json({"type": "error", "message": "Could not extract any questions from the PDF."})
            return

        await websocket.send_json({"type": "questions_found", "count": len(questions)})

        # Process each question sequentially.
        for i, question in enumerate(questions, 1):
            await websocket.send_json({"type": "status", "message": f"Processing question {i}/{len(questions)}..."})

            relevant_docs = await analyzer.find_relevant_documents(question)
            await analyzer.analyze_question(question, relevant_docs, websocket)

        await websocket.send_json({"type": "status", "message": "Analysis complete."})

    except WebSocketDisconnect:
        print("   ⚪ Client disconnected.")
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        print(f"❌ Unhandled error during WebSocket audit: {error_message}")
        traceback.print_exc()
        await websocket.send_json({"type": "error", "message": error_message})
    finally:
        # Clean up the temporary file.
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
        await websocket.close()
