import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

from rag_engine import RAGEngine
from document_processor import DocumentProcessor
from evaluation import EvaluationFramework
from cost_tracker import CostTracker
from analytics import AnalyticsDashboard

# Page configuration
st.set_page_config(
    page_title="RAG Customer Support Bot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #6b7280;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
    }
    .source-box {
        background: #f3f4f6;
        padding: 1rem;
        border-left: 4px solid #667eea;
        margin: 0.5rem 0;
        border-radius: 5px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 8px;
    }
    .stButton>button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'rag_engine' not in st.session_state:
    st.session_state.rag_engine = RAGEngine()
if 'doc_processor' not in st.session_state:
    st.session_state.doc_processor = DocumentProcessor()
if 'evaluator' not in st.session_state:
    st.session_state.evaluator = EvaluationFramework()
if 'cost_tracker' not in st.session_state:
    st.session_state.cost_tracker = CostTracker()
if 'analytics' not in st.session_state:
    st.session_state.analytics = AnalyticsDashboard()
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
with st.sidebar:
    st.image("https://img.shields.io/badge/AI-Customer%20Support-667eea?style=for-the-badge", use_column_width=True)
    
    st.markdown("### 📊 Live Metrics")
    
    # Real-time metrics
    total_queries = len(st.session_state.chat_history)
    avg_cost = st.session_state.cost_tracker.get_average_cost() if total_queries > 0 else 0
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Queries", total_queries)
    with col2:
        st.metric("Avg Cost", f"${avg_cost:.4f}")
    
    st.markdown("---")
    
    # Model selection
    st.markdown("### 🤖 Model Selection")
    model = st.selectbox(
        "Choose LLM:",
        ["GPT-4 (Best Quality)", "Claude-3 (Balanced)", "GPT-3.5 (Fast & Cheap)"],
        index=0
    )
    
    model_map = {
        "GPT-4 (Best Quality)": "gpt-4-turbo-preview",
        "Claude-3 (Balanced)": "claude-3-sonnet-20240229",
        "GPT-3.5 (Fast & Cheap)": "gpt-3.5-turbo"
    }
    
    st.session_state.rag_engine.set_model(model_map[model])
    
    st.markdown("---")
    
    # Navigation
    st.markdown("### 🧭 Navigation")
    page = st.radio(
        "Go to:",
        ["💬 Chat", "📁 Upload Documents", "📊 Analytics", "🧪 Evaluation", "💰 Cost Analysis"]
    )

# Main content
if page == "💬 Chat":
    st.markdown('<p class="main-header">🤖 RAG Customer Support Bot</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-powered support with source attribution. Upload your docs and start chatting!</p>', unsafe_allow_html=True)
    
    # Chat interface
    st.markdown("### 💬 Ask a Question")
    
    query = st.text_area(
        "Enter your question:",
        placeholder="e.g., What are the pricing plans? How do I reset my password?",
        height=100
    )
    
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        submit = st.button("🚀 Ask AI", type="primary")
    with col2:
        clear = st.button("🗑️ Clear Chat")
    
    if clear:
        st.session_state.chat_history = []
        st.rerun()
    
    if submit and query:
        with st.spinner("🤔 Thinking... (Retrieving relevant docs + Generating answer)"):
            start_time = time.time()
            
            # Get response from RAG
            result = st.session_state.rag_engine.query(query)
            
            end_time = time.time()
            latency = end_time - start_time
            
            # Track cost
            cost = st.session_state.cost_tracker.track_query(
                query, 
                result['tokens_used'], 
                model_map[model]
            )
            
            # Log to analytics
            st.session_state.analytics.log_query(
                query=query,
                response=result['answer'],
                sources=result['sources'],
                latency=latency,
                cost=cost,
                model=model_map[model]
            )
            
            # Add to history
            st.session_state.chat_history.append({
                'query': query,
                'answer': result['answer'],
                'sources': result['sources'],
                'latency': latency,
                'cost': cost,
                'timestamp': datetime.now()
            })
    
    # Display chat history
    if st.session_state.chat_history:
        st.markdown("### 💭 Conversation History")
        
        for i, chat in enumerate(reversed(st.session_state.chat_history)):
            with st.expander(f"Q: {chat['query'][:60]}...", expanded=(i==0)):
                st.markdown(f"**🤖 Answer:**\n{chat['answer']}")
                
                if chat['sources']:
                    st.markdown("**📚 Sources:**")
                    for source in chat['sources']:
                        st.markdown(f"""
                        <div class="source-box">
                            <b>{source['title']}</b><br>
                            Relevance: {source['score']:.2f}<br>
                            <small>{source['snippet'][:150]}...</small>
                        </div>
                        """, unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"⏱️ **Latency:** {chat['latency']:.2f}s")
                with col2:
                    st.markdown(f"💰 **Cost:** ${chat['cost']:.4f}")
                with col3:
                    # Feedback buttons
                    feedback = st.feedback("thumbs", key=f"feedback_{i}")
                    if feedback is not None:
                        st.session_state.analytics.log_feedback(chat['query'], feedback)

elif page == "📁 Upload Documents":
    st.markdown("### 📁 Upload Knowledge Base Documents")
    
    uploaded_files = st.file_uploader(
        "Upload your support documents (PDF, TXT, CSV):",
        type=['pdf', 'txt', 'csv', 'json'],
        accept_multiple_files=True
    )
    
    if uploaded_files:
        st.markdown(f"📄 **{len(uploaded_files)} files uploaded**")
        
        if st.button("🔄 Process & Index Documents"):
            with st.spinner("🔄 Processing documents... (Chunking + Embedding + Indexing)"):
                progress_bar = st.progress(0)
                
                for i, file in enumerate(uploaded_files):
                    # Process document
                    chunks = st.session_state.doc_processor.process(file)
                    
                    # Add to vector DB
                    st.session_state.rag_engine.add_documents(chunks)
                    
                    progress_bar.progress((i + 1) / len(uploaded_files))
                
                st.success(f"✅ Successfully indexed {len(uploaded_files)} documents!")
                st.info(f"📊 Total chunks indexed: {st.session_state.rag_engine.get_document_count()}")

elif page == "📊 Analytics":
    st.markdown("### 📊 Live Analytics Dashboard")
    
    # Get analytics data
    data = st.session_state.analytics.get_dashboard_data()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Queries", data['total_queries'])
    with col2:
        st.metric("Avg Response Time", f"{data['avg_latency']:.2f}s")
    with col3:
        st.metric("User Satisfaction", f"{data['satisfaction_rate']:.1%}")
    with col4:
        st.metric("Total Cost", f"${data['total_cost']:.2f}")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📈 Queries Over Time")
        if data['queries_over_time']:
            fig = px.line(
                data['queries_over_time'], 
                x='timestamp', 
                y='count',
                title="Query Volume"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data yet. Start chatting!")
    
    with col2:
        st.markdown("#### 💰 Cost Per Query Trend")
        if data['cost_trend']:
            fig = px.line(
                data['cost_trend'],
                x='timestamp',
                y='cost',
                title="Cost Trend"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Top topics
    st.markdown("#### 🏷️ Top Query Topics")
    if data['top_topics']:
        fig = px.bar(
            data['top_topics'],
            x='topic',
            y='count',
            title="Most Common Topics"
        )
        st.plotly_chart(fig, use_container_width=True)

elif page == "🧪 Evaluation":
    st.markdown("### 🧪 Model Evaluation Framework")
    
    st.markdown("""
    Test the RAG system with pre-defined questions to measure:
    - Answer Relevance
    - Source Attribution Accuracy
    - Hallucination Rate
    - Response Latency
    """)
    
    if st.button("🧪 Run Evaluation Suite"):
        with st.spinner("Running evaluation on test dataset..."):
            results = st.session_state.evaluator.run_evaluation(
                st.session_state.rag_engine
            )
            
            st.markdown("#### 📊 Evaluation Results")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Avg Relevance", f"{results['avg_relevance']:.2f}")
            with col2:
                st.metric("Hallucination Rate", f"{results['hallucination_rate']:.1%}")
            with col3:
                st.metric("Source Attribution", f"{results['source_attribution']:.1%}")
            with col4:
                st.metric("Avg Latency", f"{results['avg_latency']:.2f}s")
            
            # Detailed results
            st.markdown("#### 📝 Detailed Results")
            st.dataframe(results['detailed_results'])

elif page == "💰 Cost Analysis":
    st.markdown("### 💰 Cost Analysis & Optimization")
    
    cost_data = st.session_state.cost_tracker.get_analysis()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 💵 Cost Breakdown")
        fig = px.pie(
            cost_data['breakdown'],
            values='cost',
            names='component',
            title="Cost by Component"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 💸 Cost per Query Trend")
        if cost_data['per_query_trend']:
            fig = px.line(
                cost_data['per_query_trend'],
                x='timestamp',
                y='cost',
                title="Cost Efficiency"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Optimization suggestions
    st.markdown("#### 💡 Cost Optimization Suggestions")
    
    suggestions = st.session_state.cost_tracker.get_optimization_suggestions()
    for suggestion in suggestions:
        st.info(f"💡 {suggestion}")

# Footer
st.markdown("---")
st.markdown(
    "Built by **Umar Ranginwala** | "
    "[LinkedIn](https://www.linkedin.com/in/umarranginwala/?skipRedirect=true) | "
    "[GitHub](https://github.com/umarranginwala)"
)
