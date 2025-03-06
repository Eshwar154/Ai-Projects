from fastapi import APIRouter, UploadFile, File
from services.speech import transcribe_audio, synthesize_speech

router = APIRouter(prefix="/voice", tags=["Voice"])

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    text = transcribe_audio(await file.read())
    return {"transcription": text}

@router.post("/speak")
async def speak(text: dict):
    audio_data = synthesize_speech(text["content"])
    return {"audio": audio_data}

voice_router = APIRouter()

@voice_router.post("/")
async def process_voice_input(data: dict):
    # Your logic to process voice input goes here
    return {"response": "Voice input processed"}
