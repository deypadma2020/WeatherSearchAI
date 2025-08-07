# main.py

import os
import requests
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Load environment variables from .env file (optional)
load_dotenv()

# Weather tool definition
@tool
def get_weather_data(city: str) -> str:
    """
    Fetches the current weather data for a given city.
    """
    api_key = os.getenv("WEATHERSTACK_API_KEY")
    url = f'https://api.weatherstack.com/current?access_key={api_key}&query={city}'
    response = requests.get(url)
    return response.json()


# Search tool
search_tool = DuckDuckGoSearchRun()

# Groq LLM configuration
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0
)

def main():
    # Ask user for a location
    place = input("Enter the name of a place (e.g., 'Madhya Pradesh'): ").strip()

    if not place:
        print("No place entered. Exiting.")
        return

    query = f"Find the capital of {place}, then find its current weather condition"

    # Pull ReAct agent prompt from LangChain Hub
    prompt = hub.pull("hwchase17/react")

    # Create the ReAct agent
    agent = create_react_agent(
        llm=llm,
        tools=[search_tool, get_weather_data],
        prompt=prompt
    )

    # Wrap the agent into an executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=[search_tool, get_weather_data],
        verbose=True
    )

    # Execute the query
    response = agent_executor.invoke({
        "input": query
    })

    print("\nFinal Output:")
    print(response["output"])

if __name__ == "__main__":
    main()
