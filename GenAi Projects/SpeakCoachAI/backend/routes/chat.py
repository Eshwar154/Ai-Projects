from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.llm_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    text: str

@router.post("/")
async def chat_with_ai(message: ChatRequest):
    user_input = message.text
    ai_response = generate_response(user_input, role="coach")
    return {"response": ai_response}
