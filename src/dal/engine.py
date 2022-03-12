import databases
import sqlalchemy

DATABASE_URL = 'postgres://xweiyffiuiqmvd:bd1e12823896aa023ceef4fb9a9dcb46a6af15a9ebb6eb87ed56b50fdb7e0f12@ec2-34-247-151-118.eu-west-1.compute.amazonaws.com:5432/d6r40rircnqa7b'

engine = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
