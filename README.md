## Healthcare Policy Compliance Auditor

This is an AI-powered application designed to automate the process of auditing healthcare policy documents. It uses a Large Language Model (LLM) to analyze audit questions against a large corpus of policy documents and determine compliance.

### How It Works (LLM-based Matching)

1.  **Question Extraction**: The user uploads a PDF containing a list of audit questions. The backend, built with FastAPI, extracts and parses these questions.
2.  **LLM-based Document Matching**: The application sends the extracted questions along with a comprehensive list of all available policy document titles to the Gemini LLM. The LLM analyzes the semantic content of the questions and the context of the titles to identify the 1-2 most relevant policy documents for each question.
3.  **Focused Content Analysis**: For each question, the application retrieves the full text content of only the specific documents the LLM identified as relevant.
4.  **Final Compliance Analysis**: The question and the targeted document content are sent back to the LLM. The LLM then performs a detailed analysis to determine the compliance status ("Yes", "No", or "Uncertain"), provides a confidence score, a detailed explanation, and quotes the specific sections from the policy that support its conclusion.
5.  **Results**: The frontend, built with Next.js, displays the comprehensive analysis for each question.

### Technology Stack

-   **Backend**: FastAPI, Python, Uvicorn
-   **Frontend**: Next.js, React, TypeScript, Tailwind CSS
-   **Core AI**: Google AI with the Gemini 1.5 Flash model
-   **PDF Processing**: `pdfplumber`

### Directory Structure

```
.
├── backend/
│   ├── main.py           # FastAPI application
│   ├── llm_service.py    # Handles all interaction with the Google AI Gemini model
│   ├── docs.py           # Contains the list of all policy documents and their titles
│   ├── requirements.txt  # Python dependencies
│   └── .env              # Your environment file for the API key
├── frontend/
│   ├── src/app/page.tsx  # Main Next.js frontend component
│   └── ...
└── start.sh              # Main script to set up and run both frontend and backend
```

### Quick Start

1.  **Set up Environment Variables**:
    -   In the project's root directory, create a new file named `.env`.
    -   Add your Google AI API key to this `.env` file. It should look like this:
        ```
        GOOGLE_AI_API_KEY="your-google-ai-api-key"
        ```

2.  **Run the Application**:
    -   Execute the start script from the project root:
        ```bash
        ./start.sh
        ```
    -   This will:
        -   Create a Python virtual environment for the backend.
        -   Install all necessary Python and Node.js dependencies.
        -   Start the FastAPI backend server on `http://localhost:8000`.
        -   Start the Next.js frontend server on `http://localhost:3000`.

3.  **Use the Auditor**:
    -   Open your browser and navigate to `http://localhost:3000`.
    -   Upload the `Audit Questions.pdf` file.
    -   Click "Run Audit" and review the compliance analysis results.
