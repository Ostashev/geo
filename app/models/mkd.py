from sqlalchemy import Column, String

from app.core.db import Base


class Mkd(Base):
    address = Column(String())
    lat = Column(String(50))
    long = Column(String(50))

    class Config:
        orm_mode = True
