"""
Cost Tracker - Monitor API usage and costs
"""
from typing import List, Dict, Any
from datetime import datetime

class CostTracker:
    """Track and optimize API costs"""
    
    # Pricing per 1K tokens (approximate)
    PRICING = {
        'gpt-4-turbo-preview': {'input': 0.01, 'output': 0.03},
        'gpt-3.5-turbo': {'input': 0.0005, 'output': 0.0015},
        'claude-3-sonnet-20240229': {'input': 0.003, 'output': 0.015},
        'text-embedding-3-small': {'input': 0.00002, 'output': 0}
    }
    
    def __init__(self):
        self.queries = []
    
    def track_query(self, query: str, tokens_used: int, model: str) -> float:
        """Calculate and track cost for a query"""
        if model not in self.PRICING:
            model = 'gpt-3.5-turbo'  # Default fallback
        
        # Estimate input/output split (70/30)
        input_tokens = int(tokens_used * 0.7)
        output_tokens = int(tokens_used * 0.3)
        
        # Calculate cost
        pricing = self.PRICING[model]
        input_cost = (input_tokens / 1000) * pricing['input']
        output_cost = (output_tokens / 1000) * pricing['output']
        total_cost = input_cost + output_cost
        
        # Track
        self.queries.append({
            'timestamp': datetime.now(),
            'query': query,
            'tokens': tokens_used,
            'model': model,
            'cost': total_cost
        })
        
        return total_cost
    
    def get_average_cost(self) -> float:
        """Get average cost per query"""
        if not self.queries:
            return 0
        return sum(q['cost'] for q in self.queries) / len(self.queries)
    
    def get_analysis(self) -> Dict[str, Any]:
        """Get cost analysis"""
        if not self.queries:
            return {
                'breakdown': [],
                'per_query_trend': [],
                'total_cost': 0
            }
        
        # Cost breakdown by model
        model_costs = {}
        for q in self.queries:
            model = q['model']
            if model not in model_costs:
                model_costs[model] = 0
            model_costs[model] += q['cost']
        
        breakdown = [
            {'component': model, 'cost': cost}
            for model, cost in model_costs.items()
        ]
        
        # Trend
        trend = [
            {'timestamp': q['timestamp'], 'cost': q['cost']}
            for q in self.queries
        ]
        
        return {
            'breakdown': breakdown,
            'per_query_trend': trend,
            'total_cost': sum(q['cost'] for q in self.queries)
        }
    
    def get_optimization_suggestions(self) -> List[str]:
        """Get cost optimization suggestions"""
        suggestions = []
        
        if not self.queries:
            return ["Start using the system to get optimization suggestions"]
        
        avg_cost = self.get_average_cost()
        
        if avg_cost > 0.05:
            suggestions.append(
                "💰 High cost per query ($%.4f). Consider switching to GPT-3.5 for simple questions." % avg_cost
            )
        
        # Check model distribution
        models_used = {}
        for q in self.queries:
            models_used[q['model']] = models_used.get(q['model'], 0) + 1
        
        if 'gpt-4-turbo-preview' in models_used and len(self.queries) > 20:
            gpt4_percentage = models_used['gpt-4-turbo-preview'] / len(self.queries)
            if gpt4_percentage > 0.8:
                suggestions.append(
                    "🤖 80%+ queries use GPT-4. Implement query classification to route simple questions to GPT-3.5."
                )
        
        if not suggestions:
            suggestions.append("✅ Cost optimization looks good! Current spending is efficient.")
        
        return suggestions
