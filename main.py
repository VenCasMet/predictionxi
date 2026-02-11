from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List   # ✅ ADD THIS
from team_selector import generate_team

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FormationRequest(BaseModel):
    formation: str

class TeamResponse(BaseModel):
    goalkeeper: List[str]
    defenders: List[str]
    midfielders: List[str]
    attackers: List[str]


@app.post("/generate-team", response_model=TeamResponse)
def get_team(request: FormationRequest):
    return generate_team(request.formation)
