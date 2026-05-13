"""
Document Processor - Handles file upload and chunking
"""
import re
from typing import List, Dict, Any
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentProcessor:
    """Process and chunk documents for RAG indexing"""
    
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
    
    def process(self, file) -> List[Dict[str, Any]]:
        """
        Process uploaded file:
        1. Extract text
        2. Clean and normalize
        3. Chunk into pieces
        4. Add metadata
        """
        # Extract text based on file type
        if file.type == "application/pdf":
            text = self._extract_pdf(file)
        elif file.type == "text/plain":
            text = self._extract_txt(file)
        elif file.type == "text/csv":
            text = self._extract_csv(file)
        else:
            text = file.getvalue().decode('utf-8', errors='ignore')
        
        # Clean text
        text = self._clean_text(text)
        
        # Split into chunks
        chunks = self.text_splitter.split_text(text)
        
        # Add metadata
        documents = [
            {
                'text': chunk,
                'metadata': {
                    'title': file.name,
                    'chunk_id': i,
                    'source': file.name
                }
            }
            for i, chunk in enumerate(chunks)
        ]
        
        return documents
    
    def _extract_pdf(self, file) -> str:
        """Extract text from PDF"""
        try:
            import PyPDF2
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except:
            return file.getvalue().decode('utf-8', errors='ignore')
    
    def _extract_txt(self, file) -> str:
        """Extract text from TXT"""
        return file.getvalue().decode('utf-8', errors='ignore')
    
    def _extract_csv(self, file) -> str:
        """Extract text from CSV"""
        import pandas as pd
        df = pd.read_csv(file)
        return df.to_string()
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep punctuation
        text = re.sub(r'[^\w\s\.\,\?\!\-]', '', text)
        return text.strip()
