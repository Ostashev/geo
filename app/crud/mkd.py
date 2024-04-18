import requests
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crudBase import CRUDBase
from app.models import Mkd


class CRUDMkd(CRUDBase):

    
    async def request_to_geodecoder(self, address: str):
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": address,
            "format": "json"
        }

        response = requests.get(url, params=params)
        data = response.json()
        for i in data:
            if i["addresstype"] == "building":
               lat = i['lat']
               lon = i['lon']
               display_name = i['display_name']
        
        return display_name, lat, lon


    async def get_mkd_by_lat_lon(self, lat: str, lon: str, session: AsyncSession):
        mkd_info = await session.execute(select(Mkd).filter(Mkd.lat == lat, Mkd.long == lon))
        mkd_info = mkd_info.scalar()

        return mkd_info


mkd_crud = CRUDMkd(Mkd)
