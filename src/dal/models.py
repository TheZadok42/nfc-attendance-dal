from datetime import datetime

from pydantic import BaseModel


class BaseUser(BaseModel):
    first_name: str
    last_name: str
    nfc_card_uid: str


class User(BaseUser):
    id: int


class BaseAttendace(BaseModel):
    id: int
    insertion_time: datetime


class InsertAttendace(BaseModel):
    nfc_card_uid: str


class Attendace(BaseAttendace):
    user: User
