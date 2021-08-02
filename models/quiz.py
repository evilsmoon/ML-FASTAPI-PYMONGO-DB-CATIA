from typing import Optional
from pydantic import BaseModel

class Quiz(BaseModel):
    id:Optional[str]
    num:str
    profession:str
    institution:str
    answer:str
