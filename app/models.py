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
    creatives: List[str]

# Need to get new FE to save in BE nested models or id
class Campaign(BaseModel):
    campaign_id: Optional[str] = None  
    name: str
    creative_group_ids: List[str]  
    status: str = "paused"
    impressions: int = 0
