from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)


system_template= """
You are a helpful assistant that helps the user with weather information. 
"""

human_template = "{input}"


def get_agent_prompt_template() -> ChatPromptTemplate:
    prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_template),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        HumanMessagePromptTemplate.from_template(input_variables=["input"], template=human_template),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
    )
    return prompt