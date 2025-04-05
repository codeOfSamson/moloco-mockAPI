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

@router.post("/{campaign_id}/run")
def run_campaign(campaign_id: str):
    return campaign_service.run_campaign(campaign_id);
