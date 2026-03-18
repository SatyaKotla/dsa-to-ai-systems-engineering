from fastapi import FastAPI

from system_design.route_optimizer.api.routes.route_api import router as route_router

app = FastAPI(title="ButterBiscuit API 🍪", version="1.0")

app.include_router(route_router)
