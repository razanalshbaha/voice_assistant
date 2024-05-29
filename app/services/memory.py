from langchain.chains.conversation.memory import ConversationBufferWindowMemory


def chatbot_memory():
    return ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=3,
        return_messages=True
    )