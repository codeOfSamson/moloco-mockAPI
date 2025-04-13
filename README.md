# moloco-mockAPI
Features:
FastAPI Service Layer
Clean separation of routes and service logic using FastAPI.

In-Memory Data Storage
Simulated DB for campaigns, creative_groups, creatives, and a champion_waitlist.

Run Campaign Logic
Automatically generates performance metrics (impressions, clicks, conversions) when a campaign is run.

Attach Creative Groups
API endpoint to associate multiple creative groups with a specific campaign.

Full Campaign Retrieval
Combines campaign, group, and creative data into a single API call for efficient rendering on the frontend.

Champion Waitlist Endpoint
Stores and retrieves top-performing creative groups for strategic reuse.

Type-Safe Models
Uses Pydantic models for validation and structure across the API.


#Prerequisites:
-Python 3.9+

#Steps to run:
1) Download zip or clone this repo and navigate to project folder
2) create a virtual environment, run this command in terminal:
 
python3 -m venv venv
source venv/bin/activate  # on Mac/Linux
----
venv\Scripts\activate     # on Windows

3)Install dependencies, run this command in terminal: 
pip install -r requirements.txt

4) Run the server, run this command in terminal:

uvicorn app.main:app --reload

5) API will then be available on : http://127.0.0.1:8000
