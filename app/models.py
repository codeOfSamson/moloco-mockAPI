from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class Creative(BaseModel):
    creative_id: Optional[str] = None  
    type: str
    auto_endcard: bool
    file_url: str

class CreativeGroup(BaseModel):
    creative_group_id: Optional[str] = None 
    name: str
    creative_ids: List[str]
    creatives: Optional[List[Creative]] = []  


class Campaign(BaseModel):
    campaign_id: Optional[str] = None  
    name: str
    creative_group_ids: List[str]  
    status: str = "paused"
    impressions: int = 0
    creative_groups: Optional[List[CreativeGroup]] = [] 


class AttachGroupsRequest(BaseModel):
    creative_group_ids: List[str]
