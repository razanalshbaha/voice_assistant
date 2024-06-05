# from app.schemas.apis_input import WeatherInput
# from app.config import OPENWEATHERKEY
from langchain.agents import tool
from config import OPENWEATHERKEY
import requests
from config import OPENWEATHERKEY
from schemas.apis_input import WeatherInput


@tool(args_schema=WeatherInput)
async def get_weather(city: str) -> str:
    """
    Gets the weather for the specified location using the Open Meteo API.

    Args:
        city (str): The city for which to get the weather.

    Returns:
        str: The weather information for the specified location.
    """
    BASE_URL= "http://api.openweathermap.org/data/2.5/weather?"
    URL= BASE_URL + "appid=" + OPENWEATHERKEY + "&q=" + city
    try:
        response = requests.get(URL)
        data = response.json()
        return data
    except Exception as e:
        return f"An error occurred: {str(e)}"
    


    
