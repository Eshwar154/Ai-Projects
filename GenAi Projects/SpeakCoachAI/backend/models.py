from pydantic import BaseModel

class ChatRequest(BaseModel):
    text: str

class SpeechRequest(BaseModel):
    content: str

class TrainingRequest(BaseModel):
    response: str

class AssessmentRequest(BaseModel):
    content: str
