from app.agent.assistant import assistant_agent
from typing import Any
import asyncio
from app.prompts.agent_prompt import get_agent_prompt_template


async def send_message(input: str) -> Any:
    agent = await assistant_agent()
    formatted_prompt = get_agent_prompt_template().format_prompt(input= input)
    task = asyncio.create_task(
                agent.ainvoke(
                    {"input": formatted_prompt}
                )
        )
    response = await task
    return response