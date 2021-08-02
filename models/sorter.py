from typing import List, Optional
from pydantic import BaseModel

class Sorter(BaseModel):
    id:Optional[str]
    name:str
    data:List[str]
