from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
from models import User, Gender, Role
from uuid import uuid4
from uuid import UUID
from fastapi import HTTPException

app = FastAPI()

db: List[User]= [
    User(
        id=uuid4(),
        full_name= "John Doe",
        username= "johndoe",
        email= "jon@bu.edu",
        gender= Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        full_name= "Jane Doe",
        username= "janedoe",
        email= "gigi@apofis.com",
        gender= Gender.female,
        roles=[Role.admin, Role.user]
    ) 
]

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return{"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
   for user in db:
       if user.id == user_id:
           db.remove(user)
           return
       raise HTTPException(status_code=404, detail="User not found")


@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user: User):
    for u in db:
        if u.id == user_id:
            u.full_name = user.full_name
            u.username = user.username
            u.email = user.email
            return
        raise HTTPException(status_code=404, detail="User not found")
    
