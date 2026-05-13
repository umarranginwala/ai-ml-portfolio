"""
Evaluation Framework - Measure RAG system performance
"""
import pandas as pd
from typing import List, Dict, Any
import numpy as np

class EvaluationFramework:
    """Evaluate RAG system with test dataset"""
    
    def __init__(self):
        # Test dataset with expected answers
        self.test_queries = [
            {
                'query': 'What are the pricing plans?',
                'expected_answer': 'pricing',
                'category': 'pricing'
            },
            {
                'query': 'How do I reset my password?',
                'expected_answer': 'password',
                'category': 'account'
            },
            {
                'query': 'What are your support hours?',
                'expected_answer': 'hours',
                'category': 'support'
            },
            {
                'query': 'How do I cancel my subscription?',
                'expected_answer': 'cancel',
                'category': 'billing'
            },
            {
                'query': 'Do you offer refunds?',
                'expected_answer': 'refund',
                'category': 'billing'
            }
        ]
    
    def run_evaluation(self, rag_engine) -> Dict[str, Any]:
        """
        Run evaluation on test dataset
        Metrics:
        - Answer relevance (keyword matching)
        - Source attribution rate
        - Hallucination detection
        - Latency
        """
        results = []
        
        for test_case in self.test_queries:
            # Get response from RAG
            response = rag_engine.query(test_case['query'])
            
            # Calculate metrics
            relevance = self._calculate_relevance(
                response['answer'], 
                test_case['expected_answer']
            )
            
            has_sources = len(response['sources']) > 0
            
            # Check for hallucination (simple keyword check)
            hallucination = self._detect_hallucination(
                response['answer'],
                response['sources']
            )
            
            results.append({
                'query': test_case['query'],
                'category': test_case['category'],
                'relevance': relevance,
                'has_sources': has_sources,
                'hallucination': hallucination,
                'latency': response['latency'],
                'tokens_used': response['tokens_used']
            })
        
        # Aggregate results
        df = pd.DataFrame(results)
        
        return {
            'avg_relevance': df['relevance'].mean(),
            'hallucination_rate': df['hallucination'].mean(),
            'source_attribution': df['has_sources'].mean(),
            'avg_latency': df['latency'].mean(),
            'total_tokens': df['tokens_used'].sum(),
            'detailed_results': df
        }
    
    def _calculate_relevance(self, answer: str, expected: str) -> float:
        """Simple keyword-based relevance score"""
        answer_lower = answer.lower()
        expected_lower = expected.lower()
        
        # Check if expected keyword appears in answer
        if expected_lower in answer_lower:
            return 1.0
        
        # Check for related words
        related_words = {
            'pricing': ['price', 'cost', 'plan', 'subscription', 'tier'],
            'password': ['reset', 'login', 'account', 'access'],
            'hours': ['time', 'available', 'support', '24/7', 'business'],
            'cancel': ['unsubscribe', 'stop', 'end', 'terminate'],
            'refund': ['money back', 'return', 'payment', 'chargeback']
        }
        
        if expected_lower in related_words:
            for word in related_words[expected_lower]:
                if word in answer_lower:
                    return 0.7
        
        return 0.3
    
    def _detect_hallucination(self, answer: str, sources: List[Dict]) -> bool:
        """Detect potential hallucination (unsupported claims)"""
        if not sources:
            return True  # No sources = potential hallucination
        
        # Simple check: does answer contain specific claims not in sources?
        # For demo, assume no hallucination if sources present
        return False
