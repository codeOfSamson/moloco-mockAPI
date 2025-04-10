from app.database import campaigns_db, creative_groups_db, creatives_db, champion_waitlist
from app.models import Campaign
from random import randint
from typing import List


def create_campaign(campaign: Campaign):
    campaigns_db.append(campaign)
    return campaign

def get_campaigns():
    return campaigns_db

def run_campaign(campaign_id: str):
    for campaign in campaigns_db:
        if campaign.campaign_id == campaign_id:
            campaign.status = "completed"
            campaign.impressions = 0

            enriched_groups = []
            for group_id in campaign.creative_group_ids:
                group = next((g for g in creative_groups_db if g.creative_group_id == group_id), None)
                if group:
                    # Enrich with performance metrics
                    group.impressions = 10_000
                    group.clicks = randint(1000, 3000)
                    group.conversions = randint(100, group.clicks)

                    campaign.impressions += group.impressions
                    enriched_groups.append(group)

            campaign.creative_groups = enriched_groups

            return {"message": "Campaign run completed", "campaign": campaign}

    return {"error": "Campaign not found"}

def attach_creative_groups(campaign_id: str, group_ids: List[str]):
    for campaign in campaigns_db:
        if campaign.campaign_id == campaign_id:
            campaign.creative_group_ids = group_ids
            return campaign

    raise ValueError("Campaign not found")

def get_full_campaign(campaign_id: str):
    for campaign in campaigns_db:
        if campaign.campaign_id == campaign_id:
            # Fetch full creative group objects
            creative_groups = [
                group for group in creative_groups_db
                if group.creative_group_id in campaign.creative_group_ids
            ]

            # Attach full creative objects to each group
            for group in creative_groups:
                group.creatives = [
                    creative for creative in creatives_db
                    if creative.creative_id in group.creative_ids
                ]

            return {
                "campaign": campaign,
                "creative_groups": creative_groups
            }

    raise ValueError("Campaign not found")

def get_champion_waitlist():
    # Get creative groups that are in the champion waitlist
    groups = [
        group for group in creative_groups_db
        if group.creative_group_id in champion_waitlist
    ]

    # Attach full creative objects to each group
    for group in groups:
        group.creatives = [
            creative for creative in creatives_db
            if creative.creative_id in group.creative_ids
        ]

    return groups