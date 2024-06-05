
# from langchain_community.chat_message_histories import ChatMessageHistory
# def chatbot_memory():
#     memory=ChatMessageHistory()
#     return memory
# memory=chatbot_memory()


def memory(query: str, history: list =[]) -> list:
    history.append(query)
    return history