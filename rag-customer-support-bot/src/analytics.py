"""
Analytics Dashboard - Track usage and performance metrics
"""
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, Any, List
from collections import Counter

class AnalyticsDashboard:
    """Track and visualize usage analytics"""
    
    def __init__(self):
        self.queries = []
        self.feedback = []
    
    def log_query(self, query: str, response: str, sources: List[Dict], 
                  latency: float, cost: float, model: str):
        """Log a query for analytics"""
        self.queries.append({
            'timestamp': datetime.now(),
            'query': query,
            'response_length': len(response),
            'num_sources': len(sources),
            'latency': latency,
            'cost': cost,
            'model': model
        })
    
    def log_feedback(self, query: str, rating: int):
        """Log user feedback (thumbs up/down)"""
        self.feedback.append({
            'timestamp': datetime.now(),
            'query': query,
            'rating': rating  # 1 for thumbs up, 0 for thumbs down
        })
    
    def get_dashboard_data(self) -> Dict[str, Any]:
        """Get data for analytics dashboard"""
        if not self.queries:
            return {
                'total_queries': 0,
                'avg_latency': 0,
                'satisfaction_rate': 0,
                'total_cost': 0,
                'queries_over_time': [],
                'cost_trend': [],
                'top_topics': []
            }
        
        df = pd.DataFrame(self.queries)
        
        # Basic metrics
        total_queries = len(self.queries)
        avg_latency = df['latency'].mean()
        total_cost = df['cost'].sum()
        
        # Satisfaction rate
        if self.feedback:
            satisfaction_rate = sum(f['rating'] for f in self.feedback) / len(self.feedback)
        else:
            satisfaction_rate = 0
        
        # Queries over time (last 24 hours)
        now = datetime.now()
        last_24h = [q for q in self.queries if (now - q['timestamp']).days < 1]
        queries_by_hour = {}
        for q in last_24h:
            hour = q['timestamp'].strftime('%H:00')
            queries_by_hour[hour] = queries_by_hour.get(hour, 0) + 1
        
        queries_over_time = [
            {'timestamp': k, 'count': v}
            for k, v in sorted(queries_by_hour.items())
        ]
        
        # Cost trend
        cost_trend = [
            {'timestamp': q['timestamp'], 'cost': q['cost']}
            for q in self.queries[-50:]  # Last 50 queries
        ]
        
        # Top topics (simple keyword extraction)
        all_queries = ' '.join([q['query'].lower() for q in self.queries])
        common_words = ['how', 'what', 'do', 'does', 'can', 'is', 'the', 'a', 'to', 'i', 'my']
        words = [w for w in all_queries.split() if w not in common_words and len(w) > 3]
        top_words = Counter(words).most_common(10)
        
        top_topics = [
            {'topic': word, 'count': count}
            for word, count in top_words
        ]
        
        return {
            'total_queries': total_queries,
            'avg_latency': avg_latency,
            'satisfaction_rate': satisfaction_rate,
            'total_cost': total_cost,
            'queries_over_time': queries_over_time,
            'cost_trend': cost_trend,
            'top_topics': top_topics
        }
