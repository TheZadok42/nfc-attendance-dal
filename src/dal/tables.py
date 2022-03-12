import sqlalchemy
from sqlalchemy import sql

from .engine import metadata

users = sqlalchemy.Table(
    'users', metadata,
    sqlalchemy.Column('id',
                      sqlalchemy.Integer,
                      primary_key=True,
                      autoincrement=True),
    sqlalchemy.Column('first_name', sqlalchemy.Text(), nullable=False),
    sqlalchemy.Column('last_name', sqlalchemy.Text()),
    sqlalchemy.Column('nfc_card_uid',
                      sqlalchemy.Text(),
                      unique=True,
                      nullable=False))

attendance = sqlalchemy.Table(
    'attendance',
    metadata,
    sqlalchemy.Column('id',
                      sqlalchemy.Integer,
                      primary_key=True,
                      autoincrement=True),
    sqlalchemy.Column('insertion_time',
                      sqlalchemy.DateTime,
                      server_default=sql.func.now()),
    sqlalchemy.Column('user', None, sqlalchemy.ForeignKey('users.id')),
)
