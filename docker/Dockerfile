FROM tiangolo/uvicorn-gunicorn-fastapi
ENV MODULE_NAME=src.app
COPY ./ /app
COPY ./docker/prestart.sh /app/prestart.sh
RUN cd /app && python -m pip install pip && pip install -r requirements.txt