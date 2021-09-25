from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    active: Optional[bool] = True


class User(BaseUser):
    id: int


class BaseRole(BaseModel):
    role: str
    level: int


class Role(BaseRole):
    id: int


class BaseNFCCard(BaseModel):
    uid: str


class NFCCard(BaseNFCCard):
    id: int


class BaseAttendace(BaseModel):
    insertion_time: datetime
    user: int


class Attendace(BaseAttendace):
    user: User
