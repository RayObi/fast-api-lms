from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title= "Fast API LMS",
    description= "LMS for managing students and courses",
    version= "0.0.1",
    terms_of_service= "",
    contact= {
        "name": "Ray",
        "email": "raymondww90@gmail.com"

    },
    license_info= {
        "name": "Tilak Maharashtra",
    },
)


users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model=List[User])
async def get_users():
    return users




@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of the user you want to retrieve.", gt=2)):
    return users[id]