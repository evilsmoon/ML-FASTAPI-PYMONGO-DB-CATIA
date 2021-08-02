from bson.objectid import ObjectId
from fastapi import APIRouter
from config.db import  conn
from schemas.institution import institutionEntity,institutionsEntity
from models.institution import Institution
institution = APIRouter()


@institution.get('/institutions',response_model=list[Institution], tags=["institutions"])
def find_all_institution():
    return institutionsEntity(conn.catia.institution.find())

@institution.get('/institutions/{id}',response_model=Institution, tags=["institutions"])
async def find_institution(id:str):
    return institutionEntity(conn.catia.institution.find_one({"_id":ObjectId(id)}))

@institution.post('/institutions',response_model=Institution, tags=["institutions"])
async def create_institution(institution:Institution):
    new_user = dict(institution)
    del new_user['id']
    id = conn.catia.institution.insert_one(new_user).inserted_id
    return institutionEntity(conn.catia.institution.find_one({"_id":ObjectId(id)}))

