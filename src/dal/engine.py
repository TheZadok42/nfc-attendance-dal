import databases
import sqlalchemy

DATABASE_URL = 'mysql://nfc:Password1@192.168.50.131:3306/nfc'

engine = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
