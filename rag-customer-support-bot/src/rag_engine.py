"""
RAG Engine - Core retrieval and generation logic
"""
import os
from typing import List, Dict, Any
import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

class RAGEngine:
    """Retrieval-Augmented Generation Engine"""
    
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        self.model = "gpt-4-turbo-preview"
        self.documents = []  # In-memory store for demo
        
        # Custom prompt template
        self.prompt_template = PromptTemplate(
            template="""You are a helpful customer support AI assistant. Use the following pieces of context to answer the question. 
If you don't know the answer, just say you don't know. Always cite your sources.

Context:
{context}

Question: {question}

Provide a helpful, accurate answer and cite which document(s) you used:

Answer:""",
            input_variables=["context", "question"]
        )
    
    def set_model(self, model_name: str):
        """Switch between different LLMs for A/B testing"""
        self.model = model_name
    
    def add_documents(self, chunks: List[Dict[str, Any]]):
        """Add documents to the vector store"""
        for chunk in chunks:
            chunk['embedding'] = self.embeddings.embed_query(chunk['text'])
        self.documents.extend(chunks)
    
    def get_document_count(self) -> int:
        """Get total number of indexed documents"""
        return len(self.documents)
    
    def query(self, question: str) -> Dict[str, Any]:
        """
        Execute RAG query:
        1. Embed query
        2. Retrieve similar documents
        3. Generate answer with context
        4. Return answer + sources + metrics
        """
        import time
        start_time = time.time()
        
        # Step 1: Embed query
        query_embedding = self.embeddings.embed_query(question)
        
        # Step 2: Retrieve top-k similar documents (simplified cosine similarity)
        similarities = []
        for doc in self.documents:
            # Calculate cosine similarity
            import numpy as np
            similarity = np.dot(query_embedding, doc['embedding']) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(doc['embedding'])
            )
            similarities.append((similarity, doc))
        
        # Sort by similarity and get top 5
        similarities.sort(reverse=True)
        top_docs = similarities[:5]
        
        # Step 3: Prepare context
        context = "\n\n".join([
            f"[Source: {doc['metadata'].get('title', 'Unknown')}]\n{doc['text']}"
            for _, doc in top_docs
        ])
        
        # Step 4: Generate answer using OpenAI
        try:
            client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful customer support AI. Always cite your sources."
                    },
                    {
                        "role": "user",
                        "content": f"Context:\n{context}\n\nQuestion: {question}\n\nProvide a helpful answer and cite which document(s) you used:"
                    }
                ],
                temperature=0.3,
                max_tokens=1000
            )
            
            answer = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            
        except Exception as e:
            answer = f"Error generating response: {str(e)}"
            tokens_used = 0
        
        # Prepare sources
        sources = [
            {
                'title': doc['metadata'].get('title', 'Unknown'),
                'score': float(similarity),
                'snippet': doc['text'][:200]
            }
            for similarity, doc in top_docs if similarity > 0.7
        ]
        
        end_time = time.time()
        
        return {
            'answer': answer,
            'sources': sources,
            'tokens_used': tokens_used,
            'latency': end_time - start_time,
            'model_used': self.model
        }
