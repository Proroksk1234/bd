from sqlalchemy import Integer, Column, String, ForeignKey, Float, DateTime, Boolean

from bd_max.db.connect_db import Base


class ObjectTypes(Base):
    __tablename__ = "object_types"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    object_type = Column(String(60), nullable=False, unique=True)


class Districts(Base):
    __tablename__ = "districts"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    district = Column(String(60), nullable=False, unique=True)


class RealEstateObjects(Base):
    __tablename__ = "real_estate_objects"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    obj_type_id = Column(Integer, ForeignKey("object_types.id"), nullable=False)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=False)
    address = Column(String(255), nullable=False)
    square = Column(Float, nullable=False)
    cost = Column(Float, nullable=False)
    sold = Column(Boolean, nullable=False)


class DealTypes(Base):
    __tablename__ = "deal_types"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    deal_type = Column(String(255), nullable=False, unique=True)


class PeopleTypes(Base):
    __tablename__ = "people_types"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    people_type = Column(String(255), nullable=False, unique=True)


class Peoples(Base):
    __tablename__ = "peoples"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    people_type_id = Column(Integer, ForeignKey("people_types.id"), nullable=False)
    name = Column(String(60), nullable=False)
    surname = Column(String(60), nullable=False)
    patronymic = Column(String(60), nullable=False)
    email = Column(String(60), nullable=True)
    number_phone = Column(String, nullable=True)


class Deals(Base, extend_existing=True):
    __tablename__ = "deals"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    deal_type_id = Column(Integer, ForeignKey("deal_types.id"), nullable=False)
    real_estate_object_id = Column(Integer, ForeignKey("real_estate_objects.id"), nullable=False)
    buyer_id = Column(Integer, ForeignKey("peoples.id"), nullable=False)
    salesman_id = Column(Integer, ForeignKey("peoples.id"), nullable=False)
    date = Column(DateTime, nullable=False)
