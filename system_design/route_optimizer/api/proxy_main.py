from fastapi import FastAPI, HTTPException
from system_design.route_optimizer.api.models.route_request import RouteRequest
from system_design.route_optimizer.api.models.route_response import RouteResponse
import requests
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ButterBiscuit Gateway 🍪", version="1.0")

BACKEND_URL = "https://route-optimizer-api.onrender.com/route"
API_KEY = os.getenv("API_KEY")


@app.post("/route", response_model=RouteResponse, response_model_exclude_none=True)
async def proxy_route(request: RouteRequest):

    response = requests.post(
        BACKEND_URL,
        json=request.model_dump(),
        headers={"x-api-key": API_KEY, "Content-Type": "application/json"},
        timeout=10,
    )
    if response.headers.get("content-type", "").startswith("application/json"):
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


# accept frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# health check
@app.get("/health")
def health_check():
    return {"status": "ok"}
