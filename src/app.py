from fastapi import APIRouter, FastAPI

from .dal.engine import engine
from .routes import attendance_router, cards_router, roles_router, users_router

app = FastAPI(title='Attendance DAL', version='1.0.0')

admin_router = APIRouter(tags=['admin'])
admin_router.include_router(users_router)
admin_router.include_router(roles_router)
admin_router.include_router(cards_router)

app.include_router(admin_router, prefix='/admin')
app.include_router(attendance_router)


@app.get('/')
async def is_alive():
    pass


@app.on_event('startup')
async def on_start_up():
    await engine.connect()


@app.on_event('shutdown')
async def on_shutdown():
    await engine.disconnect()
