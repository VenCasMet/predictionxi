# PredictionXI Backend (FastAPI)

Live Backend URL: https://predictionxi.onrender.com/

## Overview

This backend service generates the optimal football XI squad based on
selected formation using FIFA 2017 dataset.

## Tech Stack

-   Python
-   FastAPI
-   Uvicorn
-   Pandas
-   Render Deployment

## API Endpoint

### POST /generate-team

    Request Body: { "formation": "4-3-3" }

    Response: { "goalkeeper": \["Player Name"\], "defenders": \["Player1",
    "Player2", "Player3", "Player4"\], "midfielders": \["Player1",
    "Player2", "Player3"\], "attackers": \["Player1", "Player2", "Player3"\]
    }

## Running Locally

      Clone repository
      Install dependencies: pip install -r requirements.txt
      Run server: uvicorn main:app --reload
      Visit: http://127.0.0.1:8000/docs

## CORS Configuration

CORS is enabled to allow frontend communication. For production:
allow_origins=\["\*"\] allow_credentials=False

## Deployment (Render)

-   Connected to GitHub repository
-   Start command: uvicorn main:app --host 0.0.0.0 --port \$PORT
