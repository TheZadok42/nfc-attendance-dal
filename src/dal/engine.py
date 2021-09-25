import os

import databases
import sqlalchemy

password = os.environ.get('NFC_USER_PASSWORD')

DATABASE_URL = f'mysql://nfc:{password}@nfc-database/nfc'

engine = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
