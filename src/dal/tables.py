import sqlalchemy
from sqlalchemy import sql

from .engine import metadata

users = sqlalchemy.Table(
    'users', metadata,
    sqlalchemy.Column('id',
                      sqlalchemy.Integer,
                      primary_key=True,
                      autoincrement=True),
    sqlalchemy.Column('username',
                      sqlalchemy.String(128),
                      nullable=False,
                      unique=True),
    sqlalchemy.Column('password', sqlalchemy.String(64), nullable=False),
    sqlalchemy.Column('first_name', sqlalchemy.String(256), nullable=False),
    sqlalchemy.Column('last_name', sqlalchemy.String(256)),
    sqlalchemy.Column('active', sqlalchemy.Boolean, default=True))

roles = sqlalchemy.Table(
    'roles', metadata,
    sqlalchemy.Column('id',
                      sqlalchemy.Integer,
                      primary_key=True,
                      autoincrement=True),
    sqlalchemy.Column('role', sqlalchemy.String(128), unique=True),
    sqlalchemy.Column('level', sqlalchemy.Integer, nullable=False))

users_roles = sqlalchemy.Table(
    'user_to_role', metadata,
    sqlalchemy.Column('user',
                      None,
                      sqlalchemy.ForeignKey('users.id'),
                      primary_key=True),
    sqlalchemy.Column('role',
                      None,
                      sqlalchemy.ForeignKey('roles.id'),
                      primary_key=True))

nfc_cards = sqlalchemy.Table(
    'nfc_cards',
    metadata,
    sqlalchemy.Column('id',
                      sqlalchemy.Integer,
                      primary_key=True,
                      autoincrement=True),
    sqlalchemy.Column('uid',
                      sqlalchemy.String(128),
                      unique=True,
                      nullable=False),
)

user_cards = sqlalchemy.Table(
    'user_to_card',
    metadata,
    sqlalchemy.Column('user',
                      None,
                      sqlalchemy.ForeignKey('users.id'),
                      primary_key=True),
    sqlalchemy.Column('card',
                      None,
                      sqlalchemy.ForeignKey('nfc_cards.id'),
                      primary_key=True),
)

attendance = sqlalchemy.Table(
    'attendance',
    metadata,
    sqlalchemy.Column('insertion_time',
                      sqlalchemy.DateTime,
                      primary_key=True,
                      server_default=sql.func.now()),
    sqlalchemy.Column('user', None, sqlalchemy.ForeignKey('users.id')),
)
