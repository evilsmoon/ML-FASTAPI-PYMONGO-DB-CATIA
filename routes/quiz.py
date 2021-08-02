from bson.objectid import ObjectId
from fastapi import APIRouter
from config.db import  conn
from schemas.quiz import quizEntity,quizsEntity 
from models.quiz import Quiz
from controllers.quiz import metodo
quiz = APIRouter()


@quiz.get('/quizs',response_model=list[Quiz], tags=["quiz"])
def find_all_quiz():
    # print(quizsEntity(conn.catia.quiz.find())) 
    data = []  
    for i in quizsEntity(conn.catia.quiz.find()):
        data.append(i['answer'])
    
    resp = 'Como vuelvo a repetir la psico-geriatria o geronto-psiquiatria es el puente de unión entre la parte mental y la parte neurologica; o la parte clinica, la geriatria, y la parte neurológica porque nosotros valoramos comportamiento. '
    print(metodo(resp))


@quiz.get('/quizs/{id}',response_model=Quiz, tags=["quiz"])
async def find_quiz(id:str):
    return quizEntity(conn.catia.quiz.find_one({"_id":ObjectId(id)}))

@quiz.post('/quizs',response_model=Quiz, tags=["quiz"])
async def create_quiz(quiz:Quiz):
    new_user = dict(quiz)
    del new_user['id']
    id = conn.catia.quiz.insert_one(new_user).inserted_id
    return quizEntity(conn.catia.quiz.find_one({"_id":ObjectId(id)}))

