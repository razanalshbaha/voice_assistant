# from app.services.tools.weather_tool import get_weather
# from app.services.tools.get_events_tool import get_events
# from app.services.tools.create_event_tool import create_event
# from app.services.memory import chatbot_memory
# from app.services.memory.__init__ import memory
# from app.prompts.agent_prompt import get_agent_prompt_template
# from app.services.tools.gmail_toolkit import gmail_toolkit
#from app.services.memory.add_to_chat_history import memory

# from app.config import (
#     AZURE_OPENAI_API_KEY,
#     AZURE_OPENAI_ENDPOINT,
#     AZURE_DEPLOYMENT_NAME,
#     API_VERSION,
# )


from langchain_openai import AzureChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.runnables.history import RunnableWithMessageHistory
from services.tools.weather_tool import get_weather
from services.tools.get_events_tool import get_events
from services.tools.create_event_tool import create_event
from prompts.agent_prompt import get_agent_prompt_template
from services.tools.gmail_toolkit import gmail_toolkit
from services.memory.add_to_chat_history import memory

from config import (
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

    gmailToolkit= gmail_toolkit()
    tools= [get_weather, get_events, create_event] + gmailToolkit

    agent_prompt_template = get_agent_prompt_template()
    agent = create_tool_calling_agent(llm, tools, agent_prompt_template)
    agent_executor= AgentExecutor(agent=agent, tools=tools, verbose=True)

#     agent_with_chat_history = RunnableWithMessageHistory(
#     agent_executor,
#     lambda _: memory, 
#     input_messages_key="input",
#     history_messages_key="chat_history",
# )
    return agent_executor