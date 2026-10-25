from fastapi import APIRouter

from .routes import router as general_router
from ..routers.notes import router as notes_router
from ..routers.faqs import router as faqs_router

router = APIRouter()
router.include_router(general_router)
router.include_router(notes_router)
router.include_router(faqs_router)