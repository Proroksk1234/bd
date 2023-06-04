from sqlalchemy import Integer, Column, String, ForeignKey, Float, DateTime

from bd_max.db.connect_db import Base


class TypesOfInsurance(Base):
    __tablename__ = "types_of_insurance"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    type_of_insurance = Column(String(60), nullable=False, unique=True)
    cost = Column(Float, nullable=False)


class ObjectsOfInsurance(Base):
    __tablename__ = "objects_of_insurance"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name_object = Column(String(60), nullable=False, unique=True)
    cost_object = Column(Float, nullable=False)
    type_of_insurance_id = Column(Integer, ForeignKey("types_of_insurance.id", ondelete="CASCADE"), nullable=False)

class TypesPeople(Base):
    __tablename__ = "types_people"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    type_people = Column(String, nullable=False)


class Peoples(Base):
    __tablename__ = "peoples"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    type_people_id = Column(ForeignKey("types_people.id", on_delete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    patronymic = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    number_phone = Column(String(255), nullable=True)


class InsuranceActivity(Base):
    __tablename__ = "insurance_activity"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    agent_id = Column(Integer, ForeignKey("agents.id", ondelete="CASCADE"), nullable=False)
    objects_of_insurance_id = Column(Integer, ForeignKey('objects_of_insurance.id', ondelete="CASCADE"), nullable=False)
    contract_number = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)


class PaymentsUnderTheContract(Base):
    __tablename__ = "payments_under_the_contract"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    insurance_activity_id = Column("insurance_activity_id", ForeignKey("insurance_activity.id", ondelete="CASCADE"), nullable=False)
    payments = Column(Float, nullable=False)
    received = Column(Float, nullable=False)


