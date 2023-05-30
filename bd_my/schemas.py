from pydantic import BaseModel


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class VidStrachovockSchemas(OurBaseModel):
    vid_str: str
    cost_month: int


class ObjectStrachSchemas(OurBaseModel):
    name_obj: str
    cost_obj: str
    vid_str: int


class ClientsSchemas(OurBaseModel):
    name: str
    surname: str
    otch: str
    email: str | None = None
    address: str | None = None
    number_phone: str | None = None


class AgentsSchemas(OurBaseModel):
    name: str
    surname: str
    otch: str
    email: str | None = None
    number_phone: str | None = None


class StrDeyatSchemas(OurBaseModel):
    client: int
    agent: int
    obj: int
