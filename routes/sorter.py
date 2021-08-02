from bson.objectid import ObjectId
from fastapi import APIRouter
from config.db import  conn
from schemas.sorter import sorterEntity,sortersEntity 
from models.sorter import Sorter
sorter = APIRouter()


@sorter.get('/sorter',response_model=list[Sorter], tags=["Sorter"])
def find_all_sorter():
    return sortersEntity(conn.catia.sorter.find())

@sorter.get('/sorter/{id}',response_model=Sorter, tags=["Sorter"])
async def find_sorter(id:str):
    return sorterEntity(conn.catia.sorter.find_one({"_id":ObjectId(id)}))

@sorter.post('/sorter',response_model=Sorter, tags=["Sorter"])
async def create_sorter(sorter:Sorter):
    new_user = dict(sorter)
    del new_user['id']
    id = conn.catia.sorter.insert_one(new_user).inserted_id
    return sorterEntity(conn.catia.sorter.find_one({"_id":ObjectId(id)}))

@sorter.put('/sorter',response_model=list[Sorter], tags=["Sorter"])
async def lowercase_soter():
    data = sortersEntity(conn.catia.sorter.find())

    print(data)


