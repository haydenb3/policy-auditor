## Healthcare Policy Compliance Auditor

An AI-powered application to automate healthcare policy document auditing. It uses a Large Language Model (LLM) to analyze audit questions against a corpus of policy documents and determine compliance.

**Live Application**: policy-auditor.vercel.app
- Simply upload your Audit Questions document there as a pdf, and it will do the rest!

### How It Works (LLM-based Matching)

1.  **Question Extraction**: The user uploads a PDF of audit questions. The FastAPI backend extracts and parses these questions.
2.  **LLM-based Document Matching**: The app sends questions and a list of policy titles to the Gemini LLM, which identifies the 1-2 most relevant documents for each question.
3.  **Focused Content Analysis**: The app retrieves the full text of only the relevant documents.
4.  **Final Compliance Analysis**: The question and targeted document content are sent back to the LLM for a detailed analysis of compliance status ("Yes", "No", or "Uncertain"), confidence score, explanation, and supporting quotes.
5.  **Results**: The Next.js frontend displays the analysis for each question.

### Technology Stack

-   **Backend**: FastAPI, Python, Uvicorn
-   **Frontend**: Next.js, React, TypeScript, Tailwind CSS
-   **Core AI**: Google AI with the Gemini 2.0 Flash model
-   **PDF Processing**: `pdfplumber`

### Directory Structure

```
.
├── backend/
│   ├── main.py           # FastAPI application
│   ├── llm_service.py    # Handles all interaction with the Google AI Gemini model
│   ├── docs.py           # Contains the list of all policy documents and their titles
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── src/app/page.tsx  # Main Next.js frontend component
│   └── ...
└── start.sh              # Main script to set up and run both frontend and backend locally

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
