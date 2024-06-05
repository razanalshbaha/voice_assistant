import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def calendar_authentication():
    creds = None
    if os.path.exists("calenderToken.json"):
        creds = Credentials.from_authorized_user_file("calenderToken.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "app/credentials/calenderCredentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("calenderToken.json", "w") as token:
            token.write(creds.to_json())

    return creds

