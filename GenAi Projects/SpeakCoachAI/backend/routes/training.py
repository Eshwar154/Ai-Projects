from fastapi import APIRouter
from services.feedback import evaluate_response

router = APIRouter(prefix="/training", tags=["Training"])

@router.post("/impromptu")
async def impromptu_speaking(data: dict):
    feedback = evaluate_response(data["response"], "impromptu")
    return {"feedback": feedback}

@router.post("/storytelling")
async def storytelling(data: dict):
    feedback = evaluate_response(data["response"], "storytelling")
    return {"feedback": feedback}
