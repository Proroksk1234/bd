from fastapi import APIRouter, Depends
from fastapi.params import Body
from sqlalchemy.ext.asyncio import AsyncSession

from bd_my.bd_my.crud import crud_get_types_of_insurance, crud_get_objects_of_insurance, \
    crud_get_payments_under_the_contract, crud_get_insurance_activity, crud_get_peoples, crud_get_people_types, \
    crud_post_types_of_insurance, crud_post_objects_of_insurance, crud_post_people_types, crud_post_peoples, \
    crud_post_insurance_activity, crud_post_payments_under_the_contract, crud_update_types_of_insurance, \
    crud_update_objects_of_insurance, crud_update_people_types, crud_update_peoples, crud_update_deal_types, \
    crud_update_insurance_activity, crud_update_payments_under_the_contract, crud_delete_object_types, \
    crud_delete_types_of_insurance, crud_delete_objects_of_insurance, crud_delete_people_types, crud_delete_peoples, \
    crud_delete_insurance_activity, crud_delete_payments_under_the_contract, crud_get_all_types_columns, \
    crud_add_columns, crud_delete_columns, select_received_for_clients, select_all_peoples_life, select_objects_sum, \
    select_dynamic_imprisonment, select_all_clients_and_agents
from bd_my.db.connect_db import get_db

bd = APIRouter()


@bd.get('/get_all')
async def get_all_tables(db: AsyncSession = Depends(get_db)):
    all_types_of_insurance = await crud_get_types_of_insurance(db=db)
    all_objects_of_insurance = await crud_get_objects_of_insurance(db=db)
    all_clients = await crud_get_peoples(db=db, people_type_id=1)
    all_agents = await crud_get_peoples(db=db, people_type_id=2)
    all_insurance_activity = await crud_get_insurance_activity(db=db)
    all_payments_under_the_contract = await crud_get_payments_under_the_contract(db=db)
    return {'types_of_insurance': all_types_of_insurance, 'objects_of_insurance': all_objects_of_insurance,
            'clients': all_clients, 'agents': all_agents, 'insurance_activity': all_insurance_activity,
            'payments_under_the_contract': all_payments_under_the_contract}


@bd.get('/get_all_types_of_insurance')
async def get_all_types_of_insurance(db: AsyncSession = Depends(get_db)):
    return await crud_get_types_of_insurance(db=db)


#
@bd.get('/get_type_obj/{id_obj}')
async def get_type_obj(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_types_of_insurance(db=db, id_obj=id_obj)


@bd.get('/get_all_objects_of_insurance')
async def get_all_objects_of_insurance(db: AsyncSession = Depends(get_db)):
    return await crud_get_objects_of_insurance(db=db)


@bd.get('/get_objects_of_insurance/{id_obj}')
async def get_objects_of_insurance(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_objects_of_insurance(db=db, id_obj=id_obj)


@bd.get('/get_all_people_types')
async def get_all_people_types(db: AsyncSession = Depends(get_db)):
    return await crud_get_people_types(db=db)


@bd.get('/get_people_types/{id_obj}')
async def get_people_types(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_people_types(db=db, id_obj=id_obj)


@bd.get('/get_all_clients')
async def get_all_clients(db: AsyncSession = Depends(get_db)):
    return await crud_get_peoples(db=db, people_type_id=1)


@bd.get('/get_clients/{id_obj}')
async def get_clients(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_peoples(db=db, id_obj=id_obj, people_type_id=1)


@bd.get('/get_all_agents')
async def get_all_agents(db: AsyncSession = Depends(get_db)):
    return await crud_get_peoples(db=db, people_type_id=2)


@bd.get('/get_agents/{id_obj}')
async def get_agents(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_peoples(db=db, id_obj=id_obj, people_type_id=2)


@bd.get('/get_all_insurance_activity')
async def get_all_insurance_activity(db: AsyncSession = Depends(get_db)):
    return await crud_get_insurance_activity(db=db)


@bd.get('/get_insurance_activity/{id_obj}')
async def get_insurance_activity(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_insurance_activity(db=db, id_obj=id_obj)


@bd.get('/get_all_payments_under_the_contract')
async def get_all_payments_under_the_contract(db: AsyncSession = Depends(get_db)):
    return await crud_get_payments_under_the_contract(db=db)


@bd.get('/get_payments_under_the_contract/{id_obj}')
async def get_payments_under_the_contract(id_obj: int, db: AsyncSession = Depends(get_db)):
    return await crud_get_payments_under_the_contract(db=db, id_obj=id_obj)


@bd.post('/post_types_of_insurance')
async def post_types_of_insurance(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_types_of_insurance(data=data, db=db)


@bd.post('/post_objects_of_insurance')
async def post_objects_of_insurance(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_objects_of_insurance(data=data, db=db)


@bd.post('/post_people_types')
async def post_people_types(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_people_types(data=data, db=db)


@bd.post('/post_peoples')
async def post_peoples(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_peoples(data=data, db=db)


@bd.post('/post_insurance_activity')
async def post_insurance_activity(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_insurance_activity(data=data, db=db)


@bd.post('/post_payments_under_the_contract')
async def post_payments_under_the_contract(data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_post_payments_under_the_contract(data=data, db=db)


@bd.put('/update_types_of_insurance/{id_obj}')
async def update_types_of_insurance(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_update_types_of_insurance(id_obj=id_obj, data=data, db=db)


@bd.put('/update_objects_of_insurance/{id_obj}')
async def update_objects_of_insurance(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_update_objects_of_insurance(id_obj=id_obj, data=data, db=db)


@bd.put('/update_people_types/{id_obj}')
async def update_people_types(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_update_people_types(id_obj=id_obj, data=data, db=db)


@bd.put('/update_peoples/{id_obj}')
async def update_peoples(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_update_peoples(id_obj=id_obj, data=data, db=db)


@bd.put('/update_deal_types/{id_obj}')
async def update_deal_types(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_update_deal_types(id_obj=id_obj, data=data, db=db)


@bd.put('/update_insurance_activity/{id_obj}')
async def update_insurance_activity(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_update_insurance_activity(id_obj=id_obj, data=data, db=db)


@bd.put('/update_payments_under_the_contract/{id_obj}')
async def update_payments_under_the_contract(id_obj: int, data: dict = Body(...), db: AsyncSession = Depends(get_db)):
    await crud_update_payments_under_the_contract(id_obj=id_obj, data=data, db=db)


@bd.delete('/delete_object_types/{id_obj}')
async def delete_object_types(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_object_types(id_obj=id_obj, db=db)


@bd.delete('/delete_types_of_insurance/{id_obj}')
async def delete_types_of_insurance(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_types_of_insurance(id_obj=id_obj, db=db)


@bd.delete('/delete_objects_of_insurance/{id_obj}')
async def delete_objects_of_insurance(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_objects_of_insurance(id_obj=id_obj, db=db)


@bd.delete('/delete_people_types/{id_obj}')
async def delete_people_types(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_people_types(id_obj=id_obj, db=db)


@bd.delete('/delete_peoples/{id_obj}')
async def delete_peoples(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_peoples(id_obj=id_obj, db=db)


@bd.delete('/delete_insurance_activity/{id_obj}')
async def delete_insurance_activity(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_insurance_activity(id_obj=id_obj, db=db)


@bd.delete('/delete_payments_under_the_contract/{id_obj}')
async def delete_payments_under_the_contract(id_obj: int, db: AsyncSession = Depends(get_db)):
    await crud_delete_payments_under_the_contract(id_obj=id_obj, db=db)


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


@bd.get("/all_peoples_life")
async def all_peoples_life(db: AsyncSession = Depends(get_db)):
    return await select_all_peoples_life(db=db, life_insurance_id=1)


@bd.get("/received_for_clients")
async def received_for_clients(db: AsyncSession = Depends(get_db)):
    return await select_received_for_clients(db=db)


@bd.get("/objects_sum")
async def objects_sum(insurance_sum: int, db: AsyncSession = Depends(get_db)):
    return await select_objects_sum(db=db, insurance_sum=insurance_sum)


@bd.get("/dynamic_imprisonment")
async def dynamic_imprisonment(db: AsyncSession = Depends(get_db)):
    return await select_dynamic_imprisonment(db=db)


@bd.get("/all_clients_and_agents")
async def all_clients_and_agents(db: AsyncSession = Depends(get_db)):
    return await select_all_clients_and_agents(db=db)
