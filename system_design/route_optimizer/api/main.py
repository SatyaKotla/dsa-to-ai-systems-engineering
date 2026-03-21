from fastapi import FastAPI

from system_design.route_optimizer.api.routes.route_api import router as route_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ButterBiscuit API 🍪", version="1.0")

app.include_router(route_router)

# accept frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
