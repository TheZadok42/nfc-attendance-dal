from fastapi import APIRouter
from sqlalchemy.sql.expression import select

from ..dal.engine import engine
from ..dal.tables import attendance, nfc_cards, user_cards, users

router = APIRouter(tags=['attendance'], prefix='/attendance')


@router.post('', status_code=201)
async def add_attendance_record(uid: str):
    get_user_query = select(users.c.id).select_from(nfc_cards).join(
        user_cards, user_cards.c.card == nfc_cards.c.id).join(
            users,
            users.c.id == user_cards.c.user).where(nfc_cards.c.uid == uid)
    query = attendance.insert().values(user=get_user_query.as_scalar())
    await engine.execute(query)
