from fastapi import FastAPI
from routes.institution import institution
from routes.quiz import quiz
from routes.sorter import sorter

app = FastAPI()

app.include_router(institution)
app.include_router(quiz)
app.include_router(sorter)