from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    student = "student"
    user = "user"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    full_name: Optional[str] = None
    username: str
    email: str
    gender: Gender
    roles: List[Role]

   
 



