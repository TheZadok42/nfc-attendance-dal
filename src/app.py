import os

from fastapi import FastAPI

from .dal.engine import engine
from .routes import attendance_router, users_router

app = FastAPI(title='Attendance DAL', version='1.0.0')

app.include_router(users_router, prefix='/user', tags=['user'])
app.include_router(attendance_router, prefix='/attendace', tags=['attendace'])


@app.get('/')
async def is_alive():
    return os.environ


@app.on_event('startup')
async def on_start_up():
    await engine.connect()


@app.on_event('shutdown')
async def on_shutdown():
    await engine.disconnect()
