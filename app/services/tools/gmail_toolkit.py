from langchain_community.agent_toolkits import GmailToolkit
# from app.services.authentication.gmail_authentication import gmail_authentication
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
from services.authentication.gmail_authentication import gmail_authentication

toolkit = GmailToolkit()

def gmail_toolkit():
    gmail_authentication()
    credentials = get_gmail_credentials(
    token_file="/Users/ralshabah001/Desktop/shopping_assistantt/voice_assistant/token.json",
    scopes=[
        "https://www.googleapis.com/auth/gmail.readonly",
        "https://www.googleapis.com/auth/gmail.send",
    ],
    client_secrets_file="/Users/ralshabah001/Desktop/shopping_assistantt/voice_assistant/app/credentials/credentials.json",
)
    api_resource = build_resource_service(credentials=credentials)
    toolkit = GmailToolkit(api_resource=api_resource)
    tools = toolkit.get_tools()
    return tools