from fastapi import APIRouter

from app.api.endpoints import resources, recommand




api_router = APIRouter()
api_router.include_router(resources.router, prefix="/resource", tags=["resources"])

