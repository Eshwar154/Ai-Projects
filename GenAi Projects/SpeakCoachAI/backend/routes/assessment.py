from fastapi import APIRouter
from services.feedback import evaluate_presentation

router = APIRouter(prefix="/assessment", tags=["Assessment"])

@router.post("/")
async def assess_presentation(data: dict):
    feedback = evaluate_presentation(data["content"])
    return {"feedback": feedback}
