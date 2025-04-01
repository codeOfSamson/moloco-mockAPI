from app.database import creatives_db
from app.models import Creative

def create_creative(creative: Creative):
    creatives_db.append(creative)
    return creative

def get_creatives():
    return creatives_db
