import json
from datetime import datetime

from sqlalchemy import text


async def crud_get_types_obj(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM object_types WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From object_types")
        result = await db.execute(query)
    return await data_check(result=await crud_transform_json(result=result), db=db)


async def crud_get_deal_types(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM deal_types WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From deal_types")
        result = await db.execute(query)
    return await data_check(result=await crud_transform_json(result=result), db=db)


async def crud_get_districts(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM districts WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From districts")
        result = await db.execute(query)
    return await data_check(result=await crud_transform_json(result=result), db=db)


async def crud_get_people_types(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM people_types WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From people_types")
        result = await db.execute(query)
    return await data_check(result=await crud_transform_json(result=result), db=db)


async def crud_get_real_estate_objects(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM real_estate_objects WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From real_estate_objects")
        result = await db.execute(query)
    return await data_check(result=await crud_transform_json(result=result), db=db)


async def crud_get_peoples(db, people_type_id, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM peoples WHERE id = :id_obj and people_type_id = :people_type_id")
        result = await db.execute(query, {"id_obj": id_obj, "people_type_id": people_type_id})
    else:
        query = text("SELECT * From peoples WHERE people_type_id = :people_type_id")
        result = await db.execute(query, {"people_type_id": people_type_id})
    return await data_check(result=await crud_transform_json(result=result), db=db)


async def crud_get_deals(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM deals WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From deals")
        result = await db.execute(query)
    return await data_check(result=await crud_transform_json(result=result), db=db)


async def crud_transform_json(result):
    rows = result.fetchall()
    columns = result.keys()
    rows_dict = []
    for row in rows:
        row_dict = dict(zip(columns, row))
        if 'date' in row_dict:
            row_dict['date'] = row_dict['date'].isoformat()
        rows_dict.append(row_dict)
    return json.loads(json.dumps(rows_dict))


async def crud_post_object_types(data: dict, db):
    fields = ','.join(data.keys())
    placeholders = ','.join(f':{key}' for key in data.keys())
    query_text = f"insert into object_types ({fields}) values ({placeholders})"
    query_text = text(query_text)
    await db.execute(query_text, data)
    await db.commit()


async def crud_post_districts(data: dict, db):
    fields = ','.join(data.keys())
    placeholders = ','.join(f':{key}' for key in data.keys())
    query_text = text(f"INSERT INTO districts ({fields}) VALUES ({placeholders})")
    await db.execute(query_text, data)
    await db.commit()


async def crud_post_real_estate_objects(data: dict, db):
    fields = ','.join(data.keys())
    placeholders = ','.join(f':{key}' for key in data.keys())
    query_text = text(f"INSERT INTO real_estate_objects ({fields}) VALUES ({placeholders})")
    await db.execute(query_text, data)
    await db.commit()


async def crud_post_deal_types(data: dict, db):
    fields = ','.join(data.keys())
    placeholders = ','.join(f':{key}' for key in data.keys())
    query_text = f"INSERT INTO deal_types ({fields}) VALUES ({placeholders})"
    await db.execute(query_text, data)
    await db.commit()


async def crud_post_people_types(data: dict, db):
    fields = ','.join(data.keys())
    placeholders = ','.join(f':{key}' for key in data.keys())
    query_text = f"INSERT INTO people_types ({fields}) VALUES ({placeholders})"
    await db.execute(query_text, data)
    await db.commit()


async def crud_post_peoples(data: dict, db):
    fields = ','.join(data.keys())
    placeholders = ','.join(f':{key}' for key in data.keys())
    query_text = f"INSERT INTO peoples ({fields}) VALUES ({placeholders})"
    await db.execute(query_text, data)
    await db.commit()


async def crud_post_deals(data: dict, db):
    for key, value in data.items():
        if isinstance(value, datetime):
            data[key] = value.isoformat()

    fields = ','.join(data.keys())
    placeholders = ','.join(f':{key}' for key in data.keys())
    query_text = f"INSERT INTO deals ({fields}) VALUES ({placeholders})"
    await db.execute(query_text, data)
    await db.commit()


async def crud_update_object_types(data: dict, id_obj, db):
    set_clause = ', '.join([f"{key} = :{key}" for key in data.keys()])
    query_text = f"UPDATE object_types SET {set_clause} WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj, **data)
    await db.execute(query)
    await db.commit()


async def crud_update_districts(data: dict, id_obj, db):
    set_clause = ', '.join([f"{key} = :{key}" for key in data.keys()])
    query_text = f"UPDATE districts SET {set_clause} WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj, **data)
    await db.execute(query)
    await db.commit()


async def crud_update_real_estate_objects(data: dict, id_obj, db):
    set_clause = ', '.join([f"{key} = :{key}" for key in data.keys()])
    query_text = f"UPDATE real_estate_objects SET {set_clause} WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj, **data)
    await db.execute(query)
    await db.commit()


async def crud_update_deal_types(data: dict, id_obj, db):
    set_clause = ', '.join([f"{key} = :{key}" for key in data.keys()])
    query_text = f"UPDATE deal_types SET {set_clause} WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj, **data)
    await db.execute(query)
    await db.commit()


async def crud_update_people_types(data: dict, id_obj, db):
    set_clause = ', '.join([f"{key} = :{key}" for key in data.keys()])
    query_text = f"UPDATE people_types SET {set_clause} WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj, **data)
    await db.execute(query)
    await db.commit()


async def crud_update_peoples(data: dict, id_obj, db):
    set_clause = ', '.join([f"{key} = :{key}" for key in data.keys()])
    query_text = f"UPDATE peoples SET {set_clause} WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj, **data)
    await db.execute(query)
    await db.commit()


async def crud_update_deals(data: dict, id_obj, db):
    for key, value in data.items():
        if key =='date':
            data[key] = datetime.strptime(value, '%Y-%m-%d').date()
    set_clause = ', '.join([f"{key} = :{key}" for key in data.keys()])
    query_text = f"UPDATE deals SET {set_clause} WHERE id=:id_obj"
    print(data)
    print(set_clause)
    query = text(query_text).bindparams(id_obj=id_obj, **data)
    await db.execute(query)
    await db.commit()


async def crud_delete_object_types(id_obj, db):
    query_text = "DELETE FROM object_types WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj)
    await db.execute(query)
    await db.commit()


async def crud_delete_districts(id_obj, db):
    query_text = "DELETE FROM districts WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj)
    await db.execute(query)
    await db.commit()


async def crud_delete_real_estate_objects(id_obj, db):
    query_text = "DELETE FROM real_estate_objects WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj)
    await db.execute(query)
    await db.commit()


async def crud_delete_deal_types(id_obj, db):
    query_text = "DELETE FROM deal_types WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj)
    await db.execute(query)
    await db.commit()


async def crud_delete_people_types(id_obj, db):
    query_text = "DELETE FROM people_types WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj)
    await db.execute(query)
    await db.commit()


async def crud_delete_peoples(id_obj, db):
    query_text = "DELETE FROM peoples WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj)
    await db.execute(query)
    await db.commit()


async def crud_delete_deals(id_obj, db):
    query_text = "DELETE FROM deals WHERE id=:id_obj"
    query = text(query_text).bindparams(id_obj=id_obj)
    await db.execute(query)
    await db.commit()


async def crud_get_all_types_columns():
    return ['integer', 'varchar', 'boolean', "float", "date", "timestamp"]


async def crud_add_columns(table_name, column_name, data_type, db):
    query = text(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type}")
    await db.execute(query)
    await db.commit()


async def crud_delete_columns(table_name, column_name, db):
    query = text(f"ALTER TABLE {table_name} DROP COLUMN {column_name}")
    await db.execute(query)
    await db.commit()


async def select_all_object_sales(db):
    query = text("SELECT * FROM real_estate_objects WHERE sold = False")
    result = await db.execute(query)
    return await crud_transform_json(result=result)


async def select_saldo(db):
    query = text("""
    SELECT object_types.object_type, SUM(real_estate_objects.cost)
    FROM real_estate_objects
    JOIN object_types ON object_types.id = real_estate_objects.obj_type_id
    GROUP BY object_types.object_type
    """)
    result = await db.execute(query)
    return await crud_transform_json(result=result)


async def select_dynamic_ceil(db):
    query = text("""
        SELECT districts.district, EXTRACT(YEAR FROM deals.date) AS year, COUNT(*)
        FROM deals
        JOIN real_estate_objects ON real_estate_objects.id = deals.real_estate_object_id
        JOIN districts ON districts.id = real_estate_objects.district_id
        GROUP BY districts.district, year
        """)
    result = await db.execute(query)
    return await crud_transform_json(result=result)


async def select_buyers_salesman(db):
    query = text("""
        SELECT peoples.id, peoples.name, peoples.surname, peoples.patronymic, 
            buyers.count AS buys_count, sellers.count AS sells_count
        FROM peoples
        LEFT JOIN (
            SELECT buyer_id, COUNT(*) AS count FROM deals GROUP BY buyer_id
        ) buyers ON buyers.buyer_id = peoples.id
        LEFT JOIN (
            SELECT salesman_id, COUNT(*) AS count FROM deals GROUP BY salesman_id
        ) sellers ON sellers.salesman_id = peoples.id
        """)
    result = await db.execute(query)
    return await crud_transform_json(result=result)


async def select_real_estate_objects_min_max_cost(db, min_cost, max_cost):
    query = f"SELECT * FROM real_estate_objects WHERE cost BETWEEN {min_cost} AND {max_cost}"
    result = await db.execute(query)
    return await crud_transform_json(result=result)


async def data_check(db, result):
    for count, i in enumerate(result):
        for _ in i:
            if _ == 'obj_type_id':
                result[count]['obj_type_id'] = await crud_get_types_obj(id_obj=result[count]['obj_type_id'], db=db)
            elif _ == 'district_id':
                result[count]['district_id'] = await crud_get_districts(id_obj=result[count]['district_id'], db=db)
            elif _ == 'people_type_id':
                result[count]['people_type_id'] = await crud_get_people_types(id_obj=result[count]['people_type_id'],
                                                                              db=db)
            elif _ == 'deal_type_id':
                result[count]['deal_type_id'] = await crud_get_deal_types(id_obj=result[count]['deal_type_id'], db=db)
            elif _ == 'real_estate_object_id':
                result[count]['real_estate_object_id'] = await crud_get_real_estate_objects(
                    id_obj=result[count]['real_estate_object_id'], db=db)
            elif _ == 'buyer_id':
                result[count]['buyer_id'] = await crud_get_peoples(id_obj=result[count]['buyer_id'], db=db,
                                                                   people_type_id=1)
            elif _ == 'salesman_id':
                result[count]['salesman_id'] = await crud_get_peoples(id_obj=result[count]['salesman_id'], db=db,
                                                                      people_type_id=2)
    return result
