from fastapi import APIRouter

from app.api.endpoints import mkd_router

main_router = APIRouter()
main_router.include_router(mkd_router, tags=['Mkd'], prefix='/mkd')
