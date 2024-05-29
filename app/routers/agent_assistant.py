from fastapi.routing import APIRouter
from app.services.get_response import send_message
#from app.schemas.user_input import Text

router = APIRouter()


@router.post("/agent_chatbot")
async def get_response(text):
    response= await send_message(text)
    return {"output": response['output']}
