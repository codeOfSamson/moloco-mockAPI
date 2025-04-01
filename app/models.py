# models.py
from pydantic import BaseModel, HttpUrl
from typing import List

class Creative(BaseModel):
    creative_id: str
    type: str
    auto_endcard: bool
    file_url: HttpUrl

class CreativeGroup(BaseModel):
    creative_group_id: str
    name: str
    creative_ids: List[str]

class Campaign(BaseModel):
    campaign_id: str
    name: str
    creative_group_ids: List[str]
    status: str = "paused"
    impressions: int = 0
