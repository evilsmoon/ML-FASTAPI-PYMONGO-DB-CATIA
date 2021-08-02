from typing import Optional
from pydantic import BaseModel

class Institution(BaseModel):
    id:Optional[str]
    cod:str
    name:str
