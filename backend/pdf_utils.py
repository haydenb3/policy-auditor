"""
This module contains utility functions for processing PDF files.
These functions are decoupled from the main application logic to allow
them to be used in build scripts without initializing the entire application.
"""
import re
import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts the full text content from a given PDF file.
    Used during build time to pre-process all policy documents.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = " ".join(page.extract_text() for page in pdf.pages if page.extract_text())
            # Clean up the text
            full_text = re.sub(r'Page\s+\d+\s+of\s+\d+', '', full_text)
            full_text = re.sub(r'\s+', ' ', full_text).strip()
            return full_text
    except Exception as e:
        print(f"❌ Error processing PDF {pdf_path}: {e}")
        return ""
