import databases
import sqlalchemy

DATABASE_URL = 'postgres://agewjmtkdkoftx:811470451404496aa962851b970f1943f972b31b7f8a168695eba0ffde7b2ec8@ec2-54-155-5-151.eu-west-1.compute.amazonaws.com:5432/d4me37f0v7drvr'

engine = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
