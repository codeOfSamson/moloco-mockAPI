from app.database import creative_groups_db
from app.models import CreativeGroup

def create_creative_group(creativeGroup: CreativeGroup):
    creative_groups_db.append(creativeGroup)
    return creativeGroup

def get_creative_groups():
    return creative_groups_db
