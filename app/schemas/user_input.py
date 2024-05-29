from langchain.pydantic_v1 import BaseModel


class Text(BaseModel):
    text: str