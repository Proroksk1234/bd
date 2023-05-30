import datetime
import os

import uvicorn
from fastapi import FastAPI
from sqlalchemy import Integer, Column, String, Float, Date, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from schemas import ObjectStrachSchemas, ClientsSchemas, VidStrachovockSchemas, AgentsSchemas, StrDeyatSchemas

BASEDIR = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('access+pyodbc:///?odbc_connect='
                       'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                       f"DBQ={BASEDIR}/db.accdb;")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class VidStrachovock(Base):
    __tablename__ = "Виды страховок"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    vid_str = Column("Вид страховки", String(60), nullable=False, unique=True)
    cost_month = Column("Стоимость за месяц", Float, nullable=False)


class ObjectStr(Base):
    __tablename__ = "Объекты страховки"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    name_obj = Column("Наименование объекта страховки", String(60), nullable=False)
    cost_obj = Column("Стоимость страховки на объект", Integer, nullable=False)
    vid_str = Column("Выбранный вид страховки", String(60), ForeignKey("Виды страховок.Вид страховки"),
                     nullable=False)


class Clients(Base):
    __tablename__ = "Клиенты"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    name = Column("Имя", String(60), nullable=False)
    surname = Column("Фамилия", String(60), nullable=False)
    otch = Column("Отчество", String(60), nullable=False)
    email = Column("E-mail", String(40), nullable=True)
    address = Column("Адрес прописки", String, nullable=True)
    number_phone = Column("Номер телефона", String, nullable=True)
    date = Column("Дата, с которой обслуживается", Date, nullable=True)


class Agents(Base):
    __tablename__ = "Агенты"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    name = Column("Имя", String(60), nullable=False)
    surname = Column("Фамилия", String(60), nullable=False)
    otch = Column("Отчество", String(60), nullable=False)
    email = Column("E-mail", String(40), nullable=True)
    number_phone = Column("Номер телефона", String, nullable=True)


class StrDeyat(Base):
    __tablename__ = "Страховая деятельность"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    client = Column("Клиент", Integer, ForeignKey("Клиенты.Уникальный индикатор"), nullable=False)
    agent = Column("Агент", Integer, ForeignKey("Агенты.Уникальный индикатор"), nullable=False)
    obj = Column("Объект страховки", Integer, ForeignKey("Объекты страховки.Уникальный индикатор"), nullable=False)
    vyp = Column("Выплаченная сумма", Float, nullable=False)
    pol = Column("Полученная сумма", Float, nullable=False)


Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post('/create_vid_str')
def create_vid_str(data: VidStrachovockSchemas):
    session.add(VidStrachovock(vid_str=data.vid_str, cost_month=data.cost_month))
    session.commit()


@app.put('/put_vid_str')
def put_vid_str(id_obj: int, data: VidStrachovockSchemas):
    vid_strachovock = session.query(VidStrachovock).filter_by(id=id_obj).first()
    vid_strachovock.vid_str = data.vid_str
    vid_strachovock.cost_month = data.cost_month
    session.commit()


@app.post('/create_obj_str')
def create_vid_str(data: ObjectStrachSchemas):
    session.add(ObjectStr(name_obj=data.name_obj, cost_obj=data.cost_obj, vid_str=data.vid_str))
    session.commit()


@app.put('/put_obj_str')
def put_vid_str(id_obj: int, data: ObjectStrachSchemas):
    obj_str = session.query(ObjectStr).filter_by(id=id_obj).first()
    obj_str.cost_obj = data.cost_obj
    obj_str.name_obj = data.name_obj
    obj_str.vid_str = data.vid_str
    session.commit()


@app.post('/create_clients')
def create_vid_str(data: ClientsSchemas):
    date = datetime.tzinfo()
    session.add(
        Clients(name=data.name, surname=data.surname, otch=data.otch, email=data.email, address=data.address,
                number_phone=data.number_phone, date=date))
    session.commit()


@app.put('/put_clients')
def put_vid_str(id_obj: int, data: ClientsSchemas):
    vid_strachovock = session.query(Clients).filter_by(id=id_obj).first()
    vid_strachovock.name = data.name
    vid_strachovock.surname = data.surname
    vid_strachovock.otch = data.otch
    vid_strachovock.email = data.email
    vid_strachovock.address = data.address
    vid_strachovock.number_phone = data.number_phone
    session.commit()


@app.post('/create_agents')
def create_vid_str(data: AgentsSchemas):
    session.add(VidStrachovock(name=data.name, surname=data.surname, otch=data.otch, email=data.email,
                               number_phone=data.number_phone))
    session.commit()


@app.post('/create_str_deyat_str')
def create_vid_str(data: StrDeyatSchemas):
    session.add(VidStrachovock(client=data.client, agent=data.agent, obj=data.obj, vyp=0.00, pol=0.00))
    session.commit()


@app.put('/put_vid_str')
def put_vid_str(id_obj: int, data: VidStrachovockSchemas):
    vid_strachovock = session.query(VidStrachovock).filter_by(id=id_obj).first()
    vid_strachovock.vid_str = data.vid_str
    vid_strachovock.cost_month = data.cost_month
    session.commit()


@app.put('/put_vid_str')
def put_vid_str(id_obj: int, data: VidStrachovockSchemas):
    vid_strachovock = session.query(VidStrachovock).filter_by(id=id_obj).first()
    vid_strachovock.vid_str = data.vid_str
    vid_strachovock.cost_month = data.cost_month
    session.commit()


@app.delete('/delete_vid_str')
def delete_vid_str(id_obj: int):
    session.delete(session.query(VidStrachovock).filter_by(id=id_obj).first())
    session.commit()


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host='127.0.0.1', log_level="debug")
