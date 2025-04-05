from fastapi import FastAPI
from app.routes import campaigns, creatives, creative_groups
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(campaigns.router, prefix="/campaigns", tags=["Campaigns"])
app.include_router(creatives.router, prefix="/creatives", tags=["Creatives"])
app.include_router(creative_groups.router, prefix="/creative-groups", tags=["Creative Groups"])

@app.get("/")
def root():
    return {"message": "Welcome to Moloco Ad Management API"}
