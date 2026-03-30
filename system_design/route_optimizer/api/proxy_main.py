###################################
# 1. Imports
###################################
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

import os
import requests

from system_design.route_optimizer.api.models.route_request import RouteRequest
from system_design.route_optimizer.api.models.route_response import RouteResponse


#################################
# 2. App Initialization
#################################
app = FastAPI(title="ButterBiscuit Gateway 🍪", version="1.0")


#################################
# 3. Middleware
#################################
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://route-optimizer-khaki.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

##################################
# 4. Rate Limiter Setup
##################################
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

app.add_middleware(SlowAPIMiddleware)


###################################
# 5. Exception Handlers
###################################
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Too many requests, Please try again later."},
        headers={
            "Access-Control-Allow-Origin": "https://route-optimizer-khaki.vercel.app",
        },
    )


##################################
# 6. Config
##################################
BACKEND_URL = "https://route-optimizer-api.onrender.com/route"
API_KEY = os.getenv("API_KEY")


####################################
# 7. Routes
####################################
@app.post("/route", response_model=RouteResponse, response_model_exclude_none=True)
@limiter.limit("10/minute")  # rate limit
async def proxy_route(request: Request, body: RouteRequest):

    response = requests.post(
        BACKEND_URL,
        json=body.model_dump(),
        headers={"x-api-key": API_KEY, "Content-Type": "application/json"},
        timeout=10,
    )
    if response.headers.get("content-type", "").startswith("application/json"):
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


#########################
# 8. Health Check
#########################
@app.get("/health")
def health_check():
    return {"status": "ok"}
