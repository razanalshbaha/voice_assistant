# from app.agent.assistant import assistant_agent
#from app.services.memory.add_to_chat_history import memory
from typing import Any
import asyncio

from services.memory.add_to_chat_history import memory
from agent.assistant import assistant_agent


async def send_message(input: str) -> Any:
    agent_executor = await assistant_agent()
    chat_history = memory(input)
    task = asyncio.create_task(
        agent_executor.ainvoke(
            {"input": input, "chat_history": chat_history},
            config={"configurable": {"session_id": "default_session"}},
        )
    )
    response = await task
    chat_history.append(response['output'])
    print(chat_history)
    return response