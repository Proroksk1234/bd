import json

from sqlalchemy import text


async def crud_get_types_obj(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM object_types WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From object_types")
        result = await db.execute(query)
    return await crud_transform_json(result=result)


async def crud_get_deal_types(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM deal_types WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From deal_types")
        result = await db.execute(query)
    return await crud_transform_json(result=result)


async def crud_get_districts(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM districts WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From districts")
        result = await db.execute(query)
    return await crud_transform_json(result=result)


async def crud_get_people_types(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM people_types WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From people_types")
        result = await db.execute(query)
    return await crud_transform_json(result=result)


async def crud_get_real_estate_objects(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM real_estate_objects WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From real_estate_objects")
        result = await db.execute(query)
    return await crud_transform_json(result=result)


async def crud_get_peoples(db, people_type_id, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM peoples WHERE id = :id_obj and people_type_id = :people_type_id")
        result = await db.execute(query, {"id_obj": id_obj}, {"people_type_id": people_type_id})
    else:
        query = text("SELECT * From peoples")
        result = await db.execute(query)
    return await crud_transform_json(result=result)


async def crud_get_deals(db, id_obj=None):
    if id_obj:
        query = text("SELECT * FROM deals WHERE id = :id_obj")
        result = await db.execute(query, {"id_obj": id_obj})
    else:
        query = text("SELECT * From deals")
        result = await db.execute(query)
    return await crud_transform_json(result=result)


async def crud_transform_json(result):
    rows = result.fetchall()
    columns = result.keys()
    rows_dict = []
    for row in rows:
        row_dict = dict(zip(columns, row))
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
    fields = ','.join(data.keys())
    placeholders = ','.join(f':{key}' for key in data.keys())
    query_text = f"INSERT INTO deals ({fields}) VALUES ({placeholders})"
    await db.execute(query_text, data)
    await db.commit()


async def crud_update_object_types(data: dict, id_obj, db):
    query_text = f"UPDATE object_types SET {data} WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query, data)
    await db.commit()


async def crud_update_districts(data: dict, id_obj, db):
    query_text = f"UPDATE districts SET {data} WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query, data)
    await db.commit()


async def crud_update_real_estate_objects(data: dict, id_obj, db):
    query_text = f"UPDATE real_estate_objects SET {data} WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query, data)
    await db.commit()


async def crud_update_deal_types(data: dict, id_obj, db):
    query_text = f"UPDATE deal_types SET {data} WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query, data)
    await db.commit()


async def crud_update_people_types(data: dict, id_obj, db):
    query_text = f"UPDATE people_types SET {data} WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query, data)
    await db.commit()


async def crud_update_peoples(data: dict, id_obj, db):
    query_text = f"UPDATE peoples SET {data} WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query, data)
    await db.commit()


async def crud_update_deals(data: dict, id_obj, db):
    query_text = f"UPDATE deals SET {data} WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query, data)
    await db.commit()


async def crud_delete_object_types(id_obj, db):
    query_text = "DELETE FROM object_types WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query)
    await db.commit()


async def crud_delete_districts(id_obj, db):
    query_text = "DELETE FROM districts WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query)
    await db.commit()


async def crud_delete_real_estate_objects(id_obj, db):
    query_text = "DELETE FROM real_estate_objects WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query)
    await db.commit()


async def crud_delete_deal_types(id_obj, db):
    query_text = "DELETE FROM deal_types WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query)
    await db.commit()


async def crud_delete_people_types(id_obj, db):
    query_text = "DELETE FROM people_types WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query)
    await db.commit()


async def crud_delete_peoples(id_obj, db):
    query_text = "DELETE FROM peoples WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query)
    await db.commit()


async def crud_delete_deals(id_obj, db):
    query_text = "DELETE FROM deals WHERE id=:id_obj"
    query = text(query_text, {'id_obj': id_obj})
    await db.execute(query)
    await db.commit()
