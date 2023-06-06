from fastapi import APIRouter, Depends
from fastapi.params import Body
from sqlalchemy.ext.asyncio import AsyncSession

from bd_max.db.connect_db import get_db
from .crud import crud_get_types_obj, crud_get_deal_types, crud_get_districts, crud_get_people_types, \
    crud_get_real_estate_objects, crud_get_peoples, crud_get_deals, crud_post_object_types, crud_post_districts, \
    crud_post_real_estate_objects, crud_post_deal_types, crud_post_people_types, crud_post_peoples, crud_post_deals, \
    crud_update_object_types, crud_update_real_estate_objects, crud_update_districts, crud_update_deal_types, \
    crud_update_people_types, crud_update_peoples, crud_update_deals, crud_delete_object_types, crud_delete_districts, \
    crud_delete_real_estate_objects, crud_delete_deal_types, crud_delete_people_types, crud_delete_peoples, \
    crud_delete_deals, crud_get_all_types_columns, crud_add_columns, crud_delete_columns, select_all_object_sales, \
    select_real_estate_objects_min_max_cost, select_buyers_salesman, select_dynamic_ceil, select_saldo

bd = APIRouter()


@bd.get('/get_all')
async def get_all_tables(db: AsyncSession = Depends(get_db)):
    all_types_obj = await crud_get_types_obj(db=db)
    all_districts = await crud_get_districts(db=db)
    all_real_estate_objects = await crud_get_real_estate_objects(db=db)
    all_deal_types = await crud_get_deal_types(db=db)
    all_people_types = await crud_get_people_types(db=db)
    all_buyer = await crud_get_peoples(db=db, people_type_id=1)
    all_sales = await crud_get_peoples(db=db, people_type_id=2)
    all_deals = await crud_get_deals(db=db)
    return {'type_obj': all_types_obj, 'deal_types': all_deal_types, 'districts': all_districts,
            'real_estate_objects': all_real_estate_objects, 'people_types': all_people_types,
            'buyer': all_buyer, 'salesman': all_sales, 'deals': all_deals}


@bd.get('/get_all_type_obj')
async def get_all_types_obj(db: AsyncSession = Depends(get_db)):
    return await crud_get_types_obj(db=db)


#
@bd.get('/get_type_obj/{id_obj}')
async def get_type_obj(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_types_obj(db=db, id_obj=id_obj)


@bd.get('/get_all_deal_types')
async def get_all_deal_types(db: AsyncSession = Depends(get_db)):
    return await crud_get_deal_types(db=db)


@bd.get('/get_deal_types/{id_obj}')
async def get_deal_types(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_deal_types(db=db, id_obj=id_obj)


@bd.get('/get_all_districts')
async def get_all_districts(db: AsyncSession = Depends(get_db)):
    return await crud_get_districts(db=db)


@bd.get('/get_districts/{id_obj}')
async def get_districts(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_districts(db=db, id_obj=id_obj)


@bd.get('/get_all_people_types')
async def get_districts(db: AsyncSession = Depends(get_db)):
    return await crud_get_people_types(db=db)


@bd.get('/get_all_real_estate_objects')
async def get_all_real_estate_objects(db: AsyncSession = Depends(get_db)):
    return await crud_get_real_estate_objects(db=db)


@bd.get('/get_real_estate_objects/{id_obj}')
async def get_real_estate_objects(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_real_estate_objects(db=db, id_obj=id_obj)


@bd.get('/get_all_buyers')
async def get_all_buyers(db: AsyncSession = Depends(get_db)):
    return await crud_get_peoples(db=db, people_type_id=1)


@bd.get('/get_buyers/{id_obj}')
async def get_buyers(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_peoples(db=db, people_type_id=1, id_obj=id_obj)


@bd.get('/get_all_salesman')
async def get_all_salesman(db: AsyncSession = Depends(get_db)):
    return await crud_get_peoples(db=db, people_type_id=2)


@bd.get('/get_salesman/{id_obj}')
async def get_salesman(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_peoples(db=db, people_type_id=2, id_obj=id_obj)


@bd.get('/get_all_deals')
async def get_all_deals(db: AsyncSession = Depends(get_db)):
    return await crud_get_deals(db=db)


@bd.get('/get_deals/{id_obj}')
async def get_all_deals(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_deals(db=db, id_obj=id_obj)


@bd.post('/post_object_types')
async def create_object_types(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_object_types(data=data, db=db)


@bd.post('/post_districts')
async def post_districts(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_districts(data=data, db=db)


@bd.post('/post_real_estate_objects')
async def post_real_estate_objects(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_real_estate_objects(data=data, db=db)


@bd.post('/post_deal_types')
async def post_deal_types(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_deal_types(data=data, db=db)


@bd.post('/post_people_types')
async def post_people_types(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_people_types(data=data, db=db)


@bd.post('/post_peoples')
async def post_peoples(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_peoples(data=data, db=db)


@bd.post('/post_deals')
async def post_deals(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_deals(data=data, db=db)


@bd.put('/update_object_types/{id_obj}')
async def update_object_types(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    for _ in data:
        await crud_update_object_types(id_obj=id_obj, data=_, db=db)


@bd.put('/update_districts/{id_obj}')
async def update_districts(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    for _ in data:
        await crud_update_districts(id_obj=id_obj, data=_, db=db)


@bd.put('/update_real_estate_objects/{id_obj}')
async def update_real_estate_objects(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    for _ in data:
        await crud_update_real_estate_objects(id_obj=id_obj, data=data, db=db)


@bd.put('/update_deal_types/{id_obj}')
async def update_deal_types(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    for _ in data:
        await crud_update_deal_types(id_obj=id_obj, data=data, db=db)


@bd.put('/update_people_types/{id_obj}')
async def update_people_types(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    for _ in data:
        await crud_update_people_types(id_obj=id_obj, data=data, db=db)


@bd.put('/update_peoples/{id_obj}')
async def update_peoples(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    for _ in data:
        await crud_update_peoples(id_obj=id_obj, data=data, db=db)


@bd.put('/update_deals/{id_obj}')
async def update_deals(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    for _ in data:
        await crud_update_deals(id_obj=id_obj, data=data, db=db)


@bd.delete('/delete_object_types/{id_obj}')
async def delete_object_types(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_object_types(id_obj=id_obj, db=db)


@bd.delete('/delete_districts/{id_obj}')
async def delete_districts(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_districts(id_obj=id_obj, db=db)


@bd.delete('/delete_real_estate_objects/{id_obj}')
async def delete_real_estate_objects(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_real_estate_objects(id_obj=id_obj, db=db)


@bd.delete('/delete_deal_types/{id_obj}')
async def delete_deal_types(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_deal_types(id_obj=id_obj, db=db)


@bd.delete('/delete_people_types/{id_obj}')
async def delete_people_types(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_people_types(id_obj=id_obj, db=db)


@bd.delete('/delete_peoples/{id_obj}')
async def delete_peoples(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_peoples(id_obj=id_obj, db=db)


@bd.delete('/delete_deals/{id_obj}')
async def delete_deals(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_deals(id_obj=id_obj, db=db)


@bd.get("/get_all_types_columns")
async def get_all_types_columns():
    return await crud_get_all_types_columns()


@bd.post("/add_columns")
async def add_columns(table_name: str = Body(...), column_name: str = Body(...), data_type: str = Body(...),
                      db: AsyncSession = Depends(get_db)):
    await crud_add_columns(table_name=table_name, column_name=column_name, data_type=data_type, db=db)


@bd.post("/delete_columns")
async def delete_columns(table_name: str = Body(...), column_name: str = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_delete_columns(table_name=table_name, column_name=column_name, db=db)


@bd.get("/all_object_sales")
async def all_object_sales(db: AsyncSession = Depends(get_db)):
    return await select_all_object_sales(db=db)


@bd.get("/saldo")
async def saldo(db: AsyncSession = Depends(get_db)):
    return await select_saldo(db=db)


@bd.get("/dynamic_ceil")
async def dynamic_ceil(db: AsyncSession = Depends(get_db)):
    return await select_dynamic_ceil(db=db)


@bd.get("/buyers_salesman")
async def buyers_salesman(db: AsyncSession = Depends(get_db)):
    return await select_buyers_salesman(db=db)


@bd.get("/real_estate_objects_min_max_cost")
async def real_estate_objects_min_max_cost(min_cost: float, max_cost: float, db: AsyncSession = Depends(get_db)):
    return await select_real_estate_objects_min_max_cost(db=db, min_cost=min_cost, max_cost=max_cost)
