import os

import uvicorn
from fastapi import FastAPI
from sqlalchemy import Integer, Column, String, Date, ForeignKey, Float, func, extract, text
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from bd_max.schemas import TypeObjectAndSdelkaSchemas, RaionSchemas, ObjSchemas, BuyAndCeilPeopleSchemas, SdelkaSchemas

BASEDIR = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('access+pyodbc:///?odbc_connect='
                       'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                       f"DBQ={BASEDIR}/db_max.accdb;")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class RequestFirst:
    def __init__(self):
        self.query_text = '''
        SELECT "Объекты недвижимости"."Уникальный индикатор", "Тип объекта", "Район", "Адрес", "Площадь", "Стоимость недвижимости"
        FROM "Объекты недвижимости"
        JOIN "Типы объектов" ON "Объекты недвижимости"."Тип объекта" = "Типы объектов"."Уникальный индикатор"
        JOIN "Районы" ON "Объекты недвижимости"."Район" = "Районы"."Уникальный индикатор"
        WHERE "Стоимость недвижимости" > 0;
        '''
        self.query = text(self.query_text)


class TypeObj(Base):
    __tablename__ = "Типы объектов"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    type = Column("Тип объекта", String(60), nullable=False, unique=True)


class Raion(Base):
    __tablename__ = "Районы"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    raion = Column("Район", String(60), nullable=False, unique=True)


class Obj(Base):
    __tablename__ = "Объекты недвижимости"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    type_obj = Column("Тип объекта", Integer, ForeignKey("Типы объектов.Уникальный индикатор"), nullable=False)
    raion = Column("Район", Integer, ForeignKey("Районы.Уникальный индикатор"), nullable=False)
    address = Column("Адрес", String(255), nullable=False)
    square = Column("Площадь", Float, nullable=False)
    cost = Column("Стоимость недвижимости", Float, nullable=False)


class TypeSdelka(Base):
    __tablename__ = "Типы сделок"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    type = Column("Тип сделки", String(60), nullable=False, unique=True)


class BuyPeople(Base):
    __tablename__ = "Покупатели"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    name = Column("Имя", String(60), nullable=False)
    surname = Column("Фамилия", String(60), nullable=False)
    otch = Column("Отчество", String(60), nullable=False)
    email = Column("E-mail", String(40), nullable=True)
    number_phone = Column("Номер телефона", String, nullable=True)


class CeilPeople(Base):
    __tablename__ = "Продавцы"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    name = Column("Имя", String(60), nullable=False)
    surname = Column("Фамилия", String(60), nullable=False)
    otch = Column("Отчество", String(60), nullable=False)
    email = Column("E-mail", String(40), nullable=True)
    number_phone = Column("Номер телефона", String, nullable=True)


class Sdelka(Base):
    __tablename__ = "Сделки"
    id = Column("Уникальный индикатор", Integer, primary_key=True, nullable=False, index=True)
    type_sd = Column("Тип сделки", Integer, ForeignKey("Типы сделок.Уникальный индикатор"), nullable=False)
    obj = Column("Объект недвижимости", Integer, ForeignKey("Объекты недвижимости.Уникальный индикатор"),
                 nullable=False)
    buy_people = Column("Покупатель", Integer, ForeignKey("Покупатели.Уникальный индикатор"), nullable=False)
    ceil_people = Column("Продавец", Integer, ForeignKey("Продавцы.Уникальный индикатор"), nullable=False)
    date = Column("Дата сделки", Date, nullable=False)


session.add(RequestFirst())
Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get('/get_all')
def get_all_tables():
    all_types_obj = get_all_types_obj()
    all_raion = get_all_raion()
    all_obj = get_all_obj()
    all_type_sdelka = get_all_types_sdelka()
    all_buy_people = get_all_buy_people()
    all_ceil_people = get_all_ceil_people()
    all_sdelka = get_all_sdelka()
    return {'type_obj': all_types_obj, 'type_sdelka': all_type_sdelka, 'raion': all_raion, 'obj': all_obj,
            'buy_people': all_buy_people, 'ceil_people': all_ceil_people, 'sdelka': all_sdelka}


@app.get('/get_all_type_obj')
def get_all_types_obj():
    return [{'id': x.id, 'type': x.type} for x in session.query(TypeObj).all()]


@app.get('/get_type_obj/{id_obj}')
def get_type_obj(id_obj):
    type_obj = session.query(TypeObj).filter_by(id=id_obj).first()
    if type_obj:
        return {'id': type_obj.id, 'type': type_obj.type}


@app.get('/get_all_type_sdelka')
def get_all_types_sdelka():
    return [{'id': x.id, 'type': x.type} for x in session.query(TypeSdelka).all()]


@app.get('/get_type_sdelka/{id_obj}')
def get_type_sdelka(id_obj):
    type_sdelka = session.query(TypeSdelka).filter_by(id=id_obj).first()
    if type_sdelka:
        return {'id': type_sdelka.id, 'type': type_sdelka.type}


@app.get('/get_all_raion')
def get_all_raion():
    return [{'id': x.id, 'raion': x.raion} for x in session.query(Raion).all()]


@app.get('/get_raion/{id_obj}')
def get_raion(id_obj):
    raion_obj = session.query(Raion).filter_by(id=id_obj).first()
    if raion_obj:
        return {'id': raion_obj.id, 'raion': raion_obj.raion}


@app.get('/get_all_obj')
def get_all_obj():
    return [{'id': x.id, 'type_obj': get_type_obj(id_obj=x.type_obj), 'raion': get_raion(id_obj=x.raion),
             'address': x.address, 'square': x.square, 'cost': x.cost} for x in session.query(Obj).all()]


@app.get('/get_raion/{id_obj}')
def get_obj(id_obj):
    obj = session.query(Obj).filter_by(id=id_obj).first()
    if obj:
        return {'id': obj.id, 'type_obj': get_type_obj(id_obj=obj.type_obj), 'raion': get_raion(id_obj=obj.raion),
                'address': obj.address, 'square': obj.square, 'cost': obj.cost}


@app.get('/get_all_buy_people')
def get_all_buy_people():
    return [{'id': x.id, 'name': x.name, 'surname': x.surname, 'otch': x.otch, 'email': x.email,
             'number_phone': x.number_phone} for x in session.query(BuyPeople).all()]


@app.get('/get_buy_people/{id_obj}')
def get_buy_people(id_obj):
    buy_people = session.query(BuyPeople).filter_by(id=id_obj).first()
    if buy_people:
        return {'id': buy_people.id, 'name': buy_people.name, 'surname': buy_people.surname, 'otch': buy_people.otch,
                'email': buy_people.email, 'number_phone': buy_people.number_phone}


@app.get('/get_all_ceil_people')
def get_all_ceil_people():
    return [{'id': x.id, 'name': x.name, 'surname': x.surname, 'otch': x.otch, 'email': x.email,
             'number_phone': x.number_phone} for x in session.query(CeilPeople).all()]


@app.get('/get_ceil_people/{id_obj}')
def get_ceil_people(id_obj):
    ceil_people = session.query(CeilPeople).filter_by(id=id_obj).first()
    if ceil_people:
        return {'id': ceil_people.id, 'name': ceil_people.name, 'surname': ceil_people.surname,
                'otch': ceil_people.otch, 'email': ceil_people.email, 'number_phone': ceil_people.number_phone}


@app.get('/get_all_sdelka')
def get_all_sdelka():
    return [{'id': x.id, 'type_sd': get_type_sdelka(id_obj=x.type_sd), 'obj': get_obj(id_obj=x.obj),
             'buy_people': get_buy_people(id_obj=x.buy_people), 'ceil_people': get_ceil_people(id_obj=x.ceil_people),
             'date': x.date} for x in session.query(CeilPeople).all()]


@app.post('/create_type_obj')
def create_type_obj(data: TypeObjectAndSdelkaSchemas):
    session.add(TypeObj(type=data.type))
    session.commit()


@app.post('/create_type_sdelka')
def create_type_obj(data: TypeObjectAndSdelkaSchemas):
    session.add(TypeSdelka(type=data.type))
    session.commit()


@app.post('/create_raion')
def create_raion(data: RaionSchemas):
    session.add(Raion(raion=data.raion))
    session.commit()


@app.post('/create_obj')
def create_obj(data: ObjSchemas):
    session.add(Obj(type_obj=data.type_obj, raion=data.raion, address=data.raion, square=data.square, cost=data.cost))
    session.commit()


@app.post('/create_buy_people')
def create_buy_people(data: BuyAndCeilPeopleSchemas):
    session.add(BuyPeople(name=data.name, surname=data.surname, otch=data.otch, email=data.email,
                          number_phone=data.number_phone))
    session.commit()


@app.post('/create_ceil_people')
def create_ceil_people(data: BuyAndCeilPeopleSchemas):
    session.add(CeilPeople(name=data.name, surname=data.surname, otch=data.otch, email=data.email,
                           number_phone=data.number_phone))
    session.commit()


@app.post('/create_sdelka')
def create_sdelka(data: SdelkaSchemas):
    session.add(Sdelka(type_sd=data.type_sd, obj=data.obj, buy_people=data.buy_people, ceil_people=data.ceil_people,
                       date=data.date))
    session.commit()


@app.put('/update_type_obj/{id_obj}')
def update_type_obj(id_obj: int, data: TypeObjectAndSdelkaSchemas):
    type_obj = session.query(TypeObj).filter_by(id=id_obj).first()
    if type_obj:
        type_obj.type = data.type
        session.commit()


@app.put('/update_type_sdelka/{id_obj}')
def update_type_sdelka(id_obj: int, data: TypeObjectAndSdelkaSchemas):
    type_sdelka = session.query(TypeSdelka).filter_by(id=id_obj).first()
    if type_sdelka:
        type_sdelka.type = data.type
        session.commit()


@app.put('/update_raion/{id_obj}')
def update_type_sdelka(id_obj: int, data: RaionSchemas):
    raion = session.query(Raion).filter_by(id=id_obj).first()
    if raion:
        raion.raion = data.raion
        session.commit()


@app.put('/update_obj/{id_obj}')
def update_obj(id_obj: int, data: ObjSchemas):
    obj = session.query(Obj).filter_by(id=id_obj).first()
    if obj:
        obj.type_obj = data.type_obj
        obj.raion = data.raion
        obj.address = data.address
        obj.square = data.square
        obj.cost = data.cost
        session.commit()


@app.put('/update_buy_people/{id_obj}')
def update_obj(id_obj: int, data: BuyAndCeilPeopleSchemas):
    buy_people = session.query(BuyPeople).filter_by(id=id_obj).first()
    if buy_people:
        buy_people.name = data.name
        buy_people.surname = data.surname
        buy_people.otch = data.otch
        buy_people.email = data.email
        buy_people.number_phone = data.number_phone
        session.commit()


@app.put('/update_ceil_people/{id_obj}')
def update_obj(id_obj: int, data: BuyAndCeilPeopleSchemas):
    ceil_people = session.query(CeilPeople).filter_by(id=id_obj).first()
    if ceil_people:
        ceil_people.name = data.name
        ceil_people.surname = data.surname
        ceil_people.otch = data.otch
        ceil_people.email = data.email
        ceil_people.number_phone = data.number_phone
        session.commit()


@app.put('/update_sdelka/{id_obj}')
def update_obj(id_obj: int, data: SdelkaSchemas):
    sdelka = session.query(Sdelka).filter_by(id=id_obj).first()
    if sdelka:
        sdelka.name = data.type_sd
        sdelka.surname = data.obj
        sdelka.otch = data.buy_people
        sdelka.email = data.ceil_people
        sdelka.number_phone = data.date
        session.commit()


@app.delete('/delete_type_obj/{id_obj}')
def delete_type_obj(id_obj: int):
    session.delete(session.query(TypeObj).filter_by(id=id_obj).first())
    session.commit()


@app.delete('/delete_type_sdelka/{id_obj}')
def delete_type_sdelka(id_obj: int):
    session.delete(session.query(TypeSdelka).filter_by(id=id_obj).first())
    session.commit()


@app.delete('/delete_raion/{id_obj}')
def delete_raion(id_obj: int):
    session.delete(session.query(Raion).filter_by(id=id_obj).first())
    session.commit()


@app.delete('/delete_obj/{id_obj}')
def delete_obj(id_obj: int):
    session.delete(session.query(Obj).filter_by(id=id_obj).first())
    session.commit()


@app.delete('/delete_buy_people/{id_obj}')
def delete_buy_people(id_obj: int):
    session.delete(session.query(BuyPeople).filter_by(id=id_obj).first())
    session.commit()


@app.delete('/delete_ceil_people/{id_obj}')
def delete_ceil_people(id_obj: int):
    session.delete(session.query(CeilPeople).filter_by(id=id_obj).first())
    session.commit()


@app.delete('/delete_sdelka/{id_obj}')
def delete_sdelka(id_obj: int):
    session.delete(session.query(Sdelka).filter_by(id=id_obj).first())
    session.commit()


@app.get('/get_obj_ceil')
def get_obj_ceil():
    return [get_obj(id_obj=x.obj) for x in session.query(Sdelka).all() if
            get_type_sdelka(id_obj=x.type_sd)['type'] == 'Продажа']


@app.get('/get_saldo')
def get_saldo():
    saldo_by_type_obj = session.query(TypeObj.type, func.sum(Sdelka.cost).label("saldo")). \
        join(Obj, TypeObj.id == Obj.type_obj). \
        join(Sdelka, Obj.id == Sdelka.obj). \
        group_by(TypeObj.type).all()
    return saldo_by_type_obj


@app.get('/get_obj_min_max')
def get_obj_min_max(min_cost: int, max_cost: int):
    return [get_obj(id_obj=x.id) for x in session.query(Obj).where(min_cost < Obj.cost < max_cost).all()]


@app.get('get_sales_by_raion')
def get_sales_by_raion():
    sales_by_raion = session.query(Raion.raion, extract('month', Sdelka.date), func.count(Sdelka.id)). \
        join(Obj, Raion.id == Obj.raion). \
        join(Sdelka, Obj.id == Sdelka.obj). \
        group_by(Raion.raion, extract('month', Sdelka.date)).all()
    return sales_by_raion


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host='127.0.0.1', log_level="debug")
