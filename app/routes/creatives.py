from fastapi import APIRouter
from app.models import Creative
from app.services import creatives_service

router = APIRouter()

@router.post("/")
def create_creative(creative: Creative):
    return creatives_service.create_creative(creative)

@router.get("/")
def get_creatives():
    return creatives_service.get_creatives()