from langchain.pydantic_v1 import BaseModel


class ResponseModel(BaseModel):
    output: str