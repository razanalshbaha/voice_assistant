from fastapi.routing import APIRouter
from app.services.get_response import send_message
from app.schemas.user_input import Text
from app.services.speech_services.speech_to_text import recognize_from_microphone
from app.services.speech_services.text_to_speech import synthesize_speech
from fastapi import HTTPException
from app.schemas.response import ResponseModel


router = APIRouter()


@router.post("/agent_chatbot_by_speech")
async def get_response():
    input = recognize_from_microphone()
    response= await send_message(input)
    synthesize_speech(response['output'])
    return ResponseModel(output=response['output'])


@router.post("/agent_chatbot")
async def get_response(text):
    response= await send_message(text)
    return ResponseModel(output=response['output'])