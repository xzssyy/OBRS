from fastapi import FastAPI

from app.api.api import api_router

app = FastAPI(
    title="OBRS", openapi_url=f"/api/openapi.json"
)

app.include_router(api_router, prefix="/api")
