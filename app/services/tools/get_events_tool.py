from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from langchain.agents import tool
# from app.services.authentication.calendar_authentication import calendar_authentication
# from app.schemas.apis_input import GetEventsInput

from services.authentication.calendar_authentication import calendar_authentication
from schemas.apis_input import GetEventsInput


@tool(args_schema=GetEventsInput)
async def get_events(timeMin: str, timeMax: str):
    """Shows basic usage of the Google Calendar API.
    Returns the start and name of the next 10 events on the user's calendar.
    Args:
        timeMin (str): The minimum time to get events in 'YYYY-MM-DDTHH:MM:SS' format.
        timeMax (str): The maximum time to get events in 'YYYY-MM-DDTHH:MM:SS' format.
    """
    creds = calendar_authentication()

    try:
        service = build("calendar", "v3", credentials=creds)
        timeMin = timeMin + "+03:00"
        timeMax = timeMax + "+03:00"

        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=timeMin,
                timeMax=timeMax,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            return "No upcoming events found."

        event_list = []
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            event_list.append({"start": start, "summary": event["summary"]})
        print(event_list)
        return event_list

    except HttpError as error:
        return f"An error occurred: {error}"