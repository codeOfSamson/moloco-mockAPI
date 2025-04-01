from fastapi import APIRouter
from app.models import Campaign
from app.services import campaign_service

router = APIRouter()

@router.post("/")
def create_campaign(campaign: Campaign):
    return campaign_service.create_campaign(campaign)

@router.get("/")
def get_campaigns():
    return campaign_service.get_campaigns()