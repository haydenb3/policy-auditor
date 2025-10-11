import re, os, pickle, pdfplumber, faiss, numpy as np
from typing import List, Dict, Any, Optional
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

EMBEDDING_MODEL = "models/text-embedding-004"
MIN_WORDS = 5

class DocProcessor:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key required")
        genai.configure(api_key=api_key)
        self.embeddings_dir = "./embeddings_storage"
        os.makedirs(self.embeddings_dir, exist_ok=True)

    def _extract_pdf(self, path: str) -> str:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        try:
            with pdfplumber.open(path) as pdf:
                return "".join(page.extract_text() or "" for page in pdf.pages)
        except:
            return ""

    def _clean_text(self, text: str) -> (str, str):
        footer = re.compile(
            r'^\s*Page \d+ of \d+.*$|'
            r'^\s*[A-Z]{2}\.\d{4}[a-z]?:.*$|'
            r'^\s*Revised: \d{2}/\d{2}/\d{4}\s*$',
            re.MULTILINE | re.IGNORECASE
        )
        text = footer.sub("", text)

        purpose = re.search(r'^\s*I\.\s*PURPOSE', text, re.MULTILINE)
        if purpose:
            text = text[purpose.start():]

        glossary_text = ""
        glossary = re.search(r'^\s*(IX|X)\.\s*GLOSSARY', text, re.MULTILINE | re.IGNORECASE)
        if glossary:
            glossary_text = text[glossary.start():]
            text = text[:glossary.start()]

        admin = [
            r'IV\.\s*ATTACHMENT\(S\)', r'V\.\s*REFERENCE\(S\)',
            r'VI\.\s*REGULATORY AGENCY APPROVAL\(S\)', r'VII\.\s*BOARD ACTION\(S\)',
            r'VIII\.\s*REVISION HISTORY'
        ]
        admin_pat = re.compile(r'^\s*(?:' + '|'.join(admin) + r')', re.MULTILINE | re.IGNORECASE)
        
        match = admin_pat.search(text)
        if match:
            text = text[:match.start()]

        return text.strip(), glossary_text.strip()

    def _chunk_glossary(self, text: str) -> List[str]:
        if not text:
            return []
        text = re.sub(r'^\s*(IX|X)\.\s*GLOSSARY\s*', '', text, flags=re.IGNORECASE)
        text = re.sub(r'^\s*Term\s+Definition\s*', '', text, flags=re.MULTILINE)
        entries = re.split(r'\n\s*\n', text.strip())
        
        chunks = []
        for entry in entries:
            lines = entry.strip().split('\n')
            if len(lines) > 1:
                chunks.append(' '.join(line.strip() for line in lines))
        return chunks

    def _chunk_content(self, text: str) -> List[str]:
        if not text:
            return []
        list_split = re.compile(r'\n(?=\s*(?:[A-Z]\.|[a-z]\.|\d+\.|\w+\)|\*|•|-)\s+)')
        initial = list_split.split(text)
        
        final = []
        for chunk in initial:
            paras = re.split(r'\n\s*\n', chunk)
            final.extend(p.strip() for p in paras if p.strip())
        return final

    def process(self, path: str) -> Optional[List[Dict[str, Any]]]:
        text = self._extract_pdf(path)
        if not text:
            return None

        main, glossary = self._clean_text(text)
        main_chunks = self._chunk_content(main)
        gloss_chunks = self._chunk_glossary(glossary)
        all_chunks = main_chunks + gloss_chunks

        filtered = [c for c in all_chunks if len(c.split()) >= MIN_WORDS]
        if not filtered:
            return None

        try:
            result = genai.embed_content(
                model=EMBEDDING_MODEL,
                content=filtered,
                task_type="RETRIEVAL_DOCUMENT"
            )
            embeddings = result['embedding']
            return [{"chunk": filtered[i], "embedding": embeddings[i]} for i in range(len(filtered))]
        except:
            return None

    def create_index(self, embeddings: List[List[float]], chunks: List[str], metadata: List[Dict]):
        if not embeddings:
            return
        
        emb_array = np.array(embeddings).astype('float32')
        dim = emb_array.shape[1]
        
        index = faiss.IndexFlatIP(dim)
        index.add(emb_array)
        
        faiss.write_index(index, os.path.join(self.embeddings_dir, "combined_policy_index.index"))
        
        meta = {
            "total_chunks": len(chunks),
            "total_documents": len(set([m["document"] for m in metadata])),
            "chunks": chunks,
            "metadata": metadata,
            "embedding_dimension": dim
        }
        
        with open(os.path.join(self.embeddings_dir, "combined_metadata.pkl"), 'wb') as f:
            pickle.dump(meta, f)

def get_pdfs():
    base = os.path.join(os.path.dirname(__file__), '..', 'Public Policies')
    pdfs = []
    for root, _, files in os.walk(base):
        for f in files:
            if f.endswith('.pdf'):
                pdfs.append(os.path.join(root, f))
    return pdfs

def main():
    api_key = os.getenv("GOOGLE_AI_API_KEY")
    if not api_key:
        exit(1)
    
    processor = DocProcessor(api_key=api_key)
    pdfs = get_pdfs()
    if not pdfs:
        return
    
    all_emb = []
    all_chunks = []
    all_meta = []
    
    for _, path in enumerate(pdfs, 1):
        fname = os.path.basename(path)
        try:
            data = processor.process(path)
            if data:
                doc = fname.replace('.pdf', '')
                for j, item in enumerate(data):
                    all_emb.append(item["embedding"])
                    all_chunks.append(item["chunk"])
                    all_meta.append({"document": doc, "chunk_id": j, "global_id": len(all_chunks) - 1})
        except:
            continue
    
    if all_emb:
        processor.create_index(all_emb, all_chunks, all_meta)

if __name__ == '__main__':
    main()