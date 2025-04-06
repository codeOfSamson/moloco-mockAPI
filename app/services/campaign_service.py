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
            campaign.impressions += randint(5000, 15000) 
            campaign.status = "completed"
            return {"message": "Campaign run completed", "campaign": campaign}
    
    return {"error": "Campaign not found"}

def update_campaign(campaign_id: str, updated_data: Campaign):
    for idx, existing in enumerate(campaigns_db):
        if existing["campaign_id"] == campaign_id:
            # Assign new IDs to creative groups and creatives if not provided
            for group in updated_data.creative_groups:
                if not group.creative_group_id:
                    group.creative_group_id = str(uuid4())
                for creative in group.creatives:
                    if not creative.creative_id:
                        creative.creative_id = str(uuid4())

            # Replace the existing campaign with updated one
            campaigns_db[idx] = updated_data.model_dump()
            return campaigns_db[idx]

    raise ValueError("Campaign not found")