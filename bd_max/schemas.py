from pydantic import BaseModel


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class TypeObjectAndSdelkaSchemas(OurBaseModel):
    type: str


class RaionSchemas(OurBaseModel):
    raion: str


class ObjSchemas(OurBaseModel):
    type_obj: int
    raion: int
    address: str
    square: float
    cost: float


class BuyAndCeilPeopleSchemas(OurBaseModel):
    name: str
    surname: str
    otch: str
    email: str | None = None
    number_phone: str | None = None


class SdelkaSchemas(OurBaseModel):
    type_sd: int
    obj: int
    buy_people: int
    ceil_people: int
    date: str
