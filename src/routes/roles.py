from fastapi import APIRouter

from ..dal.engine import engine
from ..dal.models import BaseRole, Role
from ..dal.tables import roles

router = APIRouter(tags=['roles'], prefix='/role')


@router.post('', response_model=Role)
async def create_role(role: BaseRole):
    query = roles.insert().values(**role.dict())
    inserted_id = await engine.execute(query)
    return {**role.dict(), 'id': inserted_id}
