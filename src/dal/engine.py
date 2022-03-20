import os

import databases
import sqlalchemy

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///:memory:')

engine = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
