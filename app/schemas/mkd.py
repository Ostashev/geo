from pydantic import BaseModel


class MkdCreate(BaseModel):
    address: str


class MkdCreateInDb(BaseModel):
    address: str
    lat: str
    long: str

    class Config:
        orm_mode = True


class MkdDB(MkdCreateInDb):
    id: int

    class Config:
        orm_mode = True
