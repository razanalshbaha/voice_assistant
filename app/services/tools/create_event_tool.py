from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from langchain.agents import tool
import uuid
# from app.services.authentication.calendar_authentication import calendar_authentication
# from app.schemas.apis_input import CreateEventInput


from services.authentication.calendar_authentication import calendar_authentication
from schemas.apis_input import CreateEventInput



@tool(args_schema=CreateEventInput)
async def create_event(summary: str, start_time: str, end_time: str, description: str = "", location: str = "", attendees: list = None):
    """Creates an event in the Google Calendar and adds a Google Meet link.
    Args:
        summary (str): The summary or title of the event.
        start_time (str): The start time of the event in 'YYYY-MM-DDTHH:MM:SS' format.
        end_time (str): The end time of the event in 'YYYY-MM-DDTHH:MM:SS' format.
        description (str, optional): A description of the event. Defaults to "".
        location (str, optional): The location of the event. Defaults to "".
        attendees (list, optional): A list of attendees' email addresses. Defaults to None.

    Returns:
        str: A confirmation message with the event details or an error message.
    """
    creds = calendar_authentication()

    try:
        service = build("calendar", "v3", credentials=creds)

        event = {
            "summary": summary,
            "location": location,
            "description": description,
            "start": {
                "dateTime": start_time,
                "timeZone": "Asia/Amman",
            },
            "end": {
                "dateTime": end_time,
                "timeZone": "Asia/Amman",
            },
            "attendees": [{"email": email} for email in attendees] if attendees else [],
            "conferenceData": {
                "createRequest": {
                    "conferenceSolutionKey": {
                        "type": "hangoutsMeet"
                    },
                    "requestId": str(uuid.uuid4())
                }
            }
        }

        event = service.events().insert(calendarId="primary", body=event, conferenceDataVersion=1).execute()
        return f"Event created: {event.get('htmlLink')}\nMeet Link: {event['conferenceData']['entryPoints'][0]['uri']}"

    except HttpError as error:
        return f"An error occurred: {error}"