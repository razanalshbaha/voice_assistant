from langchain.pydantic_v1 import BaseModel

class WeatherInput(BaseModel):
    city: str

class GetEventsInput(BaseModel):
    timeMin: str
    timeMax: str


class CreateEventInput(BaseModel):
    summary: str
    start_time: str
    end_time: str
    description: str
    location: str
    attendees: list
    
