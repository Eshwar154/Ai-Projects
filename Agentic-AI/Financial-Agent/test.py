import streamlit as st
from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os 
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define AI Agents
def create_agents():
    """Initialize AI agents for financial analysis and news retrieval."""
    web_search_agent = Agent(
        name="Web Search Agent",
        role="Search the web for the latest financial news",
        model=Groq(id="Llama-3.3-70b-Specdec"),
        tools=[DuckDuckGo()],
        instructions=["Always include sources and latest data"],
        show_tools_calls=True,
        markdown=True,
    )
    
    finance_agent = Agent(
        name="Finance AI Agent",
        model=Groq(id="Deepseek-R1-Distill-Llama-70b"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
        instructions=["Use tables for structured data presentation", "Summarize news concisely"],
        show_tool_calls=True,
        markdown=True,
    )
    
    return Agent(
        team=[web_search_agent, finance_agent],
        instructions=["Always provide sources", "Use a table to present financial data", "Ensure news is to the point"],
        show_tools_calls=True,
        markdown=True,
    )

# Fetch Financial Data
def get_financial_data(stock_symbol):
    """Fetch financial data, market trends, and investment insights for a given stock symbol."""
    multi_ai_agent = create_agents()
    return multi_ai_agent.run(f"Summarize analyst recommendations and share the latest news for {stock_symbol} in a structured table format. Keep news concise.")

# Streamlit UI Setup
st.set_page_config(page_title="Invesst.ai - AI-Powered Investment Search Engine", layout="wide")
st.title("📈 Invesst.ai - AI-Powered Investment Assistant")

# User Input Fields
stock_symbol = st.text_input("Enter Stock Symbol (e.g., NVDA, AAPL)", "NVDA")

# Investment Search Functionality
if st.button("Get Financial Insights"):
    with st.spinner("Fetching financial insights..."):
        response = get_financial_data(stock_symbol)
        st.markdown(response, unsafe_allow_html=True)

# Additional Features Placeholder
st.sidebar.title("🔍 Advanced Tools")
st.sidebar.markdown("- **AI-Powered Investment Search**: Get quick insights using natural language queries.")
st.sidebar.markdown("- **Customizable Screeners**: Filter investments based on valuation, sector, and ESG scores.")
st.sidebar.markdown("- **Portfolio Tracker**: Monitor your portfolio performance with AI-driven insights.")
st.sidebar.markdown("- **API Access**: Integrate Invesst.ai's data into your own applications.")


