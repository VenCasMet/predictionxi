from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from team_selector import generate_team

# ✅ FIRST create app
app = FastAPI()

# ✅ THEN define origins
origins = [
    "http://localhost:4200",
    "https://predictionxi-frontend.vercel.app"
]

# ✅ THEN add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- MODELS ----------------

class FormationRequest(BaseModel):
    formation: str

class TeamResponse(BaseModel):
    goalkeeper: List[str]
    defenders: List[str]
    midfielders: List[str]
    attackers: List[str]

# ---------------- ROUTE ----------------

@app.post("/generate-team", response_model=TeamResponse)
def get_team(request: FormationRequest):
    return generate_team(request.formation)
