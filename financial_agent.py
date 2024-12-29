# Developed by Rajnish Pandey
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

load_dotenv()
Groq.api_key = os.getenv('GROQ_API_KEY')

# web search agent
websearch_agent =  Agent(
    name="websearch",
    role="You are a web search agent. You can search the web for information.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    # backstory="You are a web search agent. You can search the web for information.",
    # allow_delegation=False
    instructions=["Always include the sources"],
    show_tool_calls=True,
    markdown=True
)

## Financial agent
financial_agent = Agent(
    name="financial",
    role="You are a financial agent. You can search for financial information.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, 
                    analyst_recommendations=True, 
                    stock_fundamentals=True,
                    company_news=True)
        ],
    # backstory="You are a financial agent. You can search for financial information.",
    # allow_delegation=False
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# multi agent
multi_ai_agent=Agent(
    team=[websearch_agent, financial_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)