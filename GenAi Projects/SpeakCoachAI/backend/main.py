from fastapi import FastAPI
from routes import chat_router, voice_router, training_router, assessment_router  # ✅ Fix import

app = FastAPI(title="Verbal Skills Trainer API")

# Include API routes
app.include_router(chat_router)
app.include_router(voice_router)
app.include_router(training_router)
app.include_router(assessment_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Verbal Skills Trainer API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


