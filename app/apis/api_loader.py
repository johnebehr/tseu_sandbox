from fastapi import APIRouter 

from app.apis.routes import search_routes

api_router = APIRouter()

api_router.include_router(search_routes.router, prefix="/members", tags=["Members"])