from bson.objectid import ObjectId
from fastapi import APIRouter
from config.db import  conn
from schemas.quiz import quizEntity,quizsEntity 
from models.quiz import Quiz
from controllers.quiz import metodo
quiz = APIRouter()


@quiz.get('/quizs',response_model=list[Quiz], tags=["quiz"])
def find_all_quiz():
    return quizsEntity(conn.catia.quiz.find())

@quiz.get('/quizs/{id}',response_model=Quiz, tags=["quiz"])
async def find_quiz(id:str):
    return quizEntity(conn.catia.quiz.find_one({"_id":ObjectId(id)}))

@quiz.post('/quizs',tags=["quiz"])
async def create_quiz(answer):
    resp = metodo(answer)
    print(resp)
    return resp

