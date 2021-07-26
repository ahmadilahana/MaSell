from fastapi import APIRouter
from schemas.user import User
from config.db import conn
from models.main import users

user = APIRouter()

@user.get("/")
async def read_user():
    return conn.execute(users.select()).fetchall()

@user.get("/users/{userId}")
async def read_user_by_id(userId: int):
    return conn.execute(users.select().where(users.c.userId == userId)).fetchall()

@user.post("/users/add")
async def create_user(user: User):
    return conn.execute(users.insert().values(
        firsName= user.firsName,
        lastName= user.lastName,
        email= user.email,
        avatarUrl= user.avatarUrl,
        countryId= user.countryId,
        countryCode= user.countryCode,
        country= user.country,
        verifyCode= user.verifyCode,
        registerAt= user.registerAt,
        deviceId= user.deviceId,
        IpAddress= user.IpAddress,
        isActived= user.isActived,
        password= user.password
    ))
    return conn.execute(users.select()).fetchall()

@user.put("/users/update{userId}")
async def update_user(id: int, user: User):
    conn.execute(users.update(
        firsName= user.fisrName,
        lastName= user.lastName,
        email= user.email,
        avatarUrl= user.avatarUrl,
        countryId= user.countryId,
        countryCode= user.countryCode,
        country= user.country,
        verifyCode= user.verifyCode,
        registerAt= user.registerAt,
        deviceId= user.deviceId,
        IpAddress= user.IpAddress,
        isActived= user.isActived,
        password= user.password
    ).where(users.c.userId == userId))
    return conn.execute(users.select()).fetchall()


@user.delete("/users/delete{userId}")
async def delete_by_id(id: int, user: User):
    conn.execute(users.delete().where(user.c.userId == userId))
    return conn.execute(users.select()).fetchall()