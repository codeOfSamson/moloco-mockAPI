from fastapi import APIRouter
from app.models import CreativeGroup
from app.services import creative_groups_service

router = APIRouter()

@router.post("/")
def create_creative_group(creativeGroup: CreativeGroup):
    return creative_groups_service.create_creative_group(creativeGroup)

@router.get("/")
def get_creative_groups():
    return creative_groups_service.get_creative_groups()