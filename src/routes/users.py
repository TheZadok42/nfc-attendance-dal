from fastapi import APIRouter
from src.dal.engine import engine
from src.dal.models import BaseUser, User
from src.dal.tables import users

router = APIRouter()


@router.get('/', response_model=list[User])
async def get_users_data():
    user_query = users.select()
    return await engine.fetch_all(user_query)


@router.post('/', response_model=User)
async def create_user(user: BaseUser):
    query = users.insert()
    primary_key = await engine.execute(query, user.dict())
    new_user_query = users.select(users.c.id == primary_key)
    return await engine.fetch_one(new_user_query)
