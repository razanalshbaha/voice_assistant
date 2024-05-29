from langchain.chains.api.base import APIChain
from langchain.chains.api import open_meteo_docs
from langchain.agents import tool
from langchain_openai import OpenAI
from app.schemas.apis_input import WeatherInput
from langchain.tools import StructuredTool
from langchain_openai import AzureChatOpenAI
from app.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_DEPLOYMENT_NAME,
    API_VERSION,
)

llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=API_VERSION,
    azure_deployment=AZURE_DEPLOYMENT_NAME,
)


@tool(args_schema=WeatherInput)
def get_weather(location: str) -> str:
    """
    Gets the weather for the specified location using the Open Meteo API.

    Args:
        location (str): The location for which to get the weather.

    Returns:
        str: The weather information for the specified location.
    """
    chain = APIChain.from_llm_and_api_docs(
    llm,
    open_meteo_docs.OPEN_METEO_DOCS,
    verbose=True,
    limit_to_domains=["https://api.open-meteo.com/"],
    )
    result= chain.invoke(f"what's the weather in {location}")
    final_result= result["output"]
    return final_result

