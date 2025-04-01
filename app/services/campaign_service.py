from app.database import campaigns_db
from app.models import Campaign

def create_campaign(campaign: Campaign):
    campaigns_db.append(campaign)
    return campaign

def get_campaigns():
    return campaigns_db
