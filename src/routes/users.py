import binascii
import hashlib
from typing import List

from fastapi import APIRouter
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.operators import in_op

from ..dal.engine import engine
from ..dal.models import BaseUser, User
from ..dal.tables import roles, user_cards, users, users_roles

router = APIRouter(tags=['users'], prefix='/user')

# TODO: env var
salt = '418e70623a725b15e570bb8a0a85f43a'


class NewUser(BaseUser):
    roles: List[str]


def _parse_password(raw_password: str):
    return binascii.hexlify(
        hashlib.scrypt(raw_password.encode(),
                       salt=binascii.unhexlify(salt),
                       n=2**14,
                       r=8,
                       p=1))


async def _get_roles(names: List[str]):
    query = roles.select().where(in_op(roles.c.role, names))
    return await engine.fetch_all(query)


@router.post('',
             response_model=User,
             response_model_exclude={'password'},
             status_code=201)
async def create_user(user: NewUser):
    user.password = _parse_password(user.password)
    query = users.insert().values(**user.dict(exclude={
        'roles',
    }))
    user_id = await engine.execute(query)
    query = users_roles.insert().values(user=user_id)
    await engine.execute_many(
        query, [dict(role=role.id) for role in await _get_roles(user.roles)])
    return {**user.dict(), 'id': user_id}


@router.put('/role', status_code=201)
async def add_roles(username: str, roles: List[str]):
    get_user_query = select(
        users.c.id).where(users.c.username == username).limit(1)
    query = users_roles.insert().values(user=get_user_query.as_scalar())
    await engine.execute_many(
        query, [dict(role=role.id) for role in await _get_roles(roles)])


@router.put('/card', status_code=201)
async def assign_card_to_user(username: str, card_id: int):
    get_user_query = select(
        users.c.id).where(users.c.username == username).limit(1)
    query = user_cards.insert().values(user=get_user_query.as_scalar(),
                                       card=card_id)
    await engine.execute(query)
