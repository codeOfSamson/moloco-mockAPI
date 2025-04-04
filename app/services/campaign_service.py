from app.database import campaigns_db
from app.models import Campaign
from random import randint


def create_campaign(campaign: Campaign):
    campaigns_db.append(campaign)
    return campaign

def get_campaigns():
    return campaigns_db

def run_campaign(campaign_id: str):
    for campaign in campaigns_db:
        if campaign.campaign_id == campaign_id:
            campaign.impressions += randint(5000, 15000)  # Simulate impressions
            campaign.status = "completed"
            return {"message": "Campaign run completed", "campaign": campaign}
    
    return {"error": "Campaign not found"}