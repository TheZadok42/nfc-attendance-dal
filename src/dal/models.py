from datetime import datetime

from pydantic import BaseModel


class BaseUser(BaseModel):
    first_name: str
    last_name: str
    nfc_card_uid: str


class User(BaseUser):
    id: int


class BaseAttendance(BaseModel):
    id: int
    insertion_time: datetime


class InsertAttendance(BaseModel):
    nfc_card_uid: str


class Attendance(BaseAttendance):
    user: User
