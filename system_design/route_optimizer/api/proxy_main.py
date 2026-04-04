###################################
# 1. Imports
###################################
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi import Depends, Header

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

import os
import requests

from system_design.route_optimizer.api.models.route_request import RouteRequest
from system_design.route_optimizer.api.models.route_response import RouteResponse

from jose import jwt

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
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"


def create_access_token(user_id: str):
    payload = {"sub": user_id}
    token = jwt.encode(payload, key=JWT_SECRET_KEY, algorithm=ALGORITHM)
    return token


##################################
# 7. JWT Authentication
##################################
@app.post("/login")
def login():
    token = create_access_token("demo_user")
    return {"access_token": token}


def verify_jwt(Authorization: str = Header(None)):
    print("Verifying JWT Authorization ...")
    if not Authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    try:
        parts = Authorization.split(" ")

        if len(parts) != 2 or parts[0] != "Bearer":
            raise HTTPException(status_code=401, detail="Invalid token format")

        token = parts[1]

        print("Token extracted")
        payload = jwt.decode(token=token, key=JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")


####################################
# 8. Routes
####################################
@app.post("/route", response_model=RouteResponse, response_model_exclude_none=True)
@limiter.limit("10/minute")  # rate limit
async def proxy_route(request: Request, body: RouteRequest, user=Depends(verify_jwt)):

    print(f"[GATEWAY] Incoming request for map ={body.map}")

    try:
        response = requests.post(
            BACKEND_URL,
            json=body.model_dump(),
            headers={"x-api-key": API_KEY, "Content-Type": "application/json"},
            timeout=10,
        )

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=503, detail="Backend unavailable")

    print(f"[GATEWAY] Response status={response.status_code}")

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    try:
        data = response.json()
    except ValueError:
        raise HTTPException(status_code=500, detail="Invalid JSON from backend")

    if not data:
        raise HTTPException(status_code=500, detail="Empty response from backend")

    return data


#########################
# 9. Health Check
#########################
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "gateway",
    }
