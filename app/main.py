from fastapi import FastAPI
from app.routes import campaigns, creatives, creative_groups

app = FastAPI()

app.include_router(campaigns.router, prefix="/campaigns", tags=["Campaigns"])
app.include_router(creatives.router, prefix="/creatives", tags=["Creatives"])
app.include_router(creative_groups.router, prefix="/creative-groups", tags=["Creative Groups"])

@app.get("/")
def root():
    return {"message": "Welcome to Moloco Ad Management API"}
