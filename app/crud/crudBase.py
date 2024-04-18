from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def create(
            self, 
            obj_in,
            session: AsyncSession,
    ):
        try:
            obj_in_data = obj_in.dict()
            db_obj = self.model(**obj_in_data)
            session.add(db_obj)
            await session.commit()
            await session.refresh(db_obj)
            return db_obj
        except IntegrityError as e:
            raise HTTPException(status_code=422, detail=f"Такой объект уже существует.")
 