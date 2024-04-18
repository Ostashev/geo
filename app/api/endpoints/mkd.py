from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.mkd import mkd_crud
from app.models import *
from app.schemas.mkd import MkdCreateInDb, MkdDB

router = APIRouter()

@router.post(
    '/create',
    response_model_exclude_none=True,
    status_code=201,
    response_model=MkdDB,
    summary="Создание нового адреса",
)
async def create_new_mkd(
        address: str = Query(..., example="Россия, Пермь, Ленина, 60"),
        session: AsyncSession = Depends(get_async_session),
):

    display_name, lat, lon = await mkd_crud.request_to_geodecoder(address)
    mkd_info = await mkd_crud.get_mkd_by_lat_lon(lat, lon, session=session)
    if mkd_info is None:
        new_mkd_info = await mkd_crud.create(
            MkdCreateInDb(address=display_name, lat=lat, long=lon),
            session=session
        )
        return new_mkd_info
    
    return mkd_info
