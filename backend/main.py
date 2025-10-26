import os, tempfile
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from llm_service import analyzer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://policy-auditor.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

@app.get("/")
def health_check():
    return {"status": "online"}


@app.websocket("/ws/audit")
async def audit(websocket: WebSocket, x_api_key: str = Query(...)):
    if x_api_key != os.getenv("API_KEY"):
        await websocket.close(code=1008)
        return

    await websocket.accept()
    temp_path = None
    
    try:
        data = await websocket.receive_bytes()
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as f:
            f.write(data)
            temp_path = f.name

        questions = analyzer.extract_questions(temp_path)
        if not questions:
            await websocket.send_json({"type": "error", "message": "No questions found in PDF"})
            return

        await websocket.send_json({"type": "questions_found", "count": len(questions)})

        for q in questions:
            await analyzer.analyze_question(q, [], websocket)
        
        await websocket.close()

    except WebSocketDisconnect:
        pass
    except Exception as e:
        await websocket.send_json({"type": "error", "message": str(e)})
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)