FROM node:23-alpine as frontend

WORKDIR /frontend

ADD ./frontend/ /frontend

RUN npm install --include=dev

FROM python:3.11-alpine as backend

WORKDIR /backend

COPY --from=frontend /frontend/build /frontend/build

ADD ./backend /backend

RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt


CMD [ "fastapi", "run", "main.py" ]