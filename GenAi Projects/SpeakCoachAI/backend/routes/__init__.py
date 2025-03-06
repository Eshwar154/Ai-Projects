from .chat import router as chat_router
from .voice import voice_router
from .training import training_router
from .assessment import assessment_router

__all__ = ["chat_router", "voice_router", "training_router", "assessment_router"]
