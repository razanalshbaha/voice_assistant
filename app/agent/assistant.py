from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from app.services.tools.weather_tool import get_weather
from langchain.agents import initialize_agent
from app.services.memory import chatbot_memory
from langchain_openai import AzureChatOpenAI
from langchain.agents import(
    create_react_agent,
    AgentExecutor
)
from app.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_DEPLOYMENT_NAME,
    API_VERSION,
)


async def assistant_agent():
    llm = AzureChatOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=API_VERSION,
        azure_deployment=AZURE_DEPLOYMENT_NAME,
    )

    conversational_agent = initialize_agent(
    agent='chat-conversational-react-description', 
    tools=get_weather, 
    llm=llm,
    verbose=True,
    max_iterations=3,
    memory=chatbot_memory
    )
    agent_executor= AgentExecutor(agent=conversational_agent, tools=get_weather,verbose=True)
    return agent_executor