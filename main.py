from fastapi import FastAPI
from route.main import user, login
# from fastapi.logger import logger

app = FastAPI()

app.include_router(user)
app.include_router(login)