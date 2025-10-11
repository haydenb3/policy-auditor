## Healthcare Policy Compliance Auditor

An AI-powered application to automate healthcare policy document auditing. It uses vector embeddings and semantic search to intelligently match audit questions with relevant policy sections, then analyzes compliance using Google's Gemini LLM.

**🚀 [Live Demo](https://policy-auditor.vercel.app)**

Simply upload your Audit Questions PDF and the system will automatically analyze compliance across 373+ policy documents.

### How It Works (Vector Embeddings + RAG)

1.  **Document Preprocessing**: All policy PDFs are processed into semantic chunks, cleaned of headers/footers, and converted to vector embeddings using Google's text-embedding-004 model.
2.  **Vector Storage**: Embeddings are stored in a FAISS index for fast similarity search across 373+ policy documents.
3.  **Question Extraction**: The user uploads a PDF of audit questions. The FastAPI backend extracts and parses these questions.
4.  **Intelligent Question Parsing**: Complex multi-part questions are automatically broken down into component parts using Gemini.
5.  **Semantic Search**: Each question part is converted to a vector embedding and searched against the FAISS index to find the most relevant policy chunks.
6.  **Context Assembly**: The most relevant chunks are assembled into a focused context for analysis.
7.  **Final Compliance Analysis**: The question and relevant policy context are sent to Gemini for detailed compliance analysis ("Yes", "No", or "Uncertain"), confidence score, explanation, and supporting quotes.
8.  **Results**: The Next.js frontend displays the analysis for each question.

### Technology Stack

-   **Backend**: FastAPI, Python, Uvicorn
-   **Frontend**: Next.js, React, TypeScript, Tailwind CSS
-   **Core AI**: Google AI with the Gemini 2.5 Flash model
-   **Vector Search**: FAISS (Facebook AI Similarity Search)
-   **Embeddings**: Google AI text-embedding-004 model
-   **PDF Processing**: `pdfplumber`
-   **Vector Storage**: FAISS index with pickle metadata

### Directory Structure

```
.
├── backend/
│   ├── main.py                    # FastAPI application with WebSocket endpoints
│   ├── llm_service.py             # Core AI logic with vector search and compliance analysis
│   ├── preprocess.py              # Document preprocessing and FAISS index generation
│   ├── embeddings_storage/        # FAISS index and metadata storage
│   │   ├── combined_policy_index.index
│   │   └── combined_metadata.pkl
│   └── requirements.txt           # Python dependencies
├── frontend/
│   ├── src/app/page.tsx           # Main Next.js frontend component
│   └── ...
├── Public Policies/               # Source policy documents (373+ PDFs)
└── start.sh                      # Main script to set up and run both frontend and backend locally

```

### Prerequisites

- Python 3.9+
- Node.js 18+
- Google AI API Key ([Get one here](https://aistudio.google.com/app/apikey))

### Quick Start

1.  **Set up Environment Variables**:
    ```bash
    # Create .env file in backend directory
    echo 'GOOGLE_AI_API_KEY="your-google-ai-api-key"' > backend/.env
    ```

2.  **Generate Vector Embeddings** (First time only):
    ```bash
    cd backend
    python3 preprocess.py
    cd ..
    ```
    This processes all 373+ PDF files and creates a FAISS index (~5-10 minutes).

3.  **Run the Application**:
    ```bash
    ./start.sh
    ```
    This will automatically:
    - Create Python virtual environment
    - Install all dependencies
    - Start backend on `http://localhost:8000`
    - Start frontend on `http://localhost:3000`

4.  **Use the App**:
    - Open `http://localhost:3000`
    - Upload an audit questions PDF
    - Review the compliance analysis results

### Key Features

- **Intelligent Question Parsing**: Automatically breaks down complex multi-part audit questions
- **Semantic Search**: Uses vector embeddings to find the most relevant policy sections
- **Real-time Processing**: WebSocket-based streaming of audit results
- **High Accuracy**: Combines semantic search with LLM analysis for precise compliance determination
- **Scalable**: Processes 373+ policy documents efficiently using FAISS vector search
