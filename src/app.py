from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .dal.engine import engine
from .routes import attendance_router, users_router

app = FastAPI(title='Attendance DAL', version='1.0.0')

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(users_router, prefix='/user', tags=['user'])
app.include_router(attendance_router,
                   prefix='/attendance',
                   tags=['attendance'])


@app.get('/')
async def is_alive():
    pass


@app.on_event('startup')
async def on_start_up():
    await engine.connect()


@app.on_event('shutdown')
async def on_shutdown():
    await engine.disconnect()
