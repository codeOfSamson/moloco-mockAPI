from fastapi import APIRouter, HTTPException
from app.models import Campaign, AttachGroupsRequest, ChampionAddRequest
from app.services import campaign_service
from typing import Dict, List
from app.database import champion_waitlist


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

@router.put("/{campaign_id}/attach-groups")
def attach_creative_groups(campaign_id: str, data: AttachGroupsRequest):
    try:
        return campaign_service.attach_creative_groups(campaign_id, data.creative_group_ids)
    except ValueError:
        raise HTTPException(status_code=404, detail="Campaign not found")
@router.get("/{campaign_id}/full")
def get_full_campaign(campaign_id: str):
    try:
        return campaign_service.get_full_campaign(campaign_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Campaign not found")

@router.post("/champion-waitlist/add")
def add_to_champion_waitlist(data: ChampionAddRequest):
    group_id = data.group_id
    if group_id not in champion_waitlist:
        champion_waitlist.append(group_id)
    return {"message": "Added to champion waitlist", "waitlist": champion_waitlist}

@router.get("/champion-waitlist")
def get_champion_waitlist():
    return {
        "groups": campaign_service.get_champion_waitlist()
    }
