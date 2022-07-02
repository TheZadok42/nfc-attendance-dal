from fastapi import APIRouter
from sqlalchemy import select
from src.dal.engine import engine
from src.dal.models import Attendance, InsertAttendance, User
from src.dal.tables import attendance, users

router = APIRouter()


@router.get('/', response_model=list[Attendance])
async def get_attendances():
    query = select(attendance, users).select_from(attendance).join(
        users, users.c.id == attendance.c.user)
    cursor = await engine.fetch_all(query)
    results = list()
    for record in cursor:
        attendance_model = _parse_raw_attendance_record(record)
        results.append(attendance_model)
    return results


@router.post('/', response_model=Attendance)
async def insert_attendance(new_attendance: InsertAttendance):
    query = attendance.insert()
    user_subquery = select(users.c.id).where(
        users.c.nfc_card_uid == new_attendance.nfc_card_uid).scalar_subquery()
    primary_key = await engine.execute(query, dict(user=user_subquery))
    new_attendance_query = select(attendance,
                                  users).select_from(attendance).join(
                                      users,
                                      users.c.id == attendance.c.user).where(
                                          attendance.c.id == primary_key)
    record = await engine.fetch_one(new_attendance_query)
    return _parse_raw_attendance_record(record)


def _parse_raw_attendance_record(record) -> Attendance:
    user_model = User(id=record.user,
                      first_name=record.first_name,
                      last_name=record.last_name,
                      nfc_card_uid=record.nfc_card_uid)
    attendance_model = Attendance(id=record.id,
                                  insertion_time=record.insertion_time,
                                  user=user_model)
    return attendance_model
