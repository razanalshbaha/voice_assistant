from langchain.pydantic_v1 import BaseModel

class WeatherInput(BaseModel):
    input: str

