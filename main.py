from fastapi import FastAPI
from route.main import user

app = FastAPI()

app.include_router(user)