from fastapi import APIRouter, Request
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
async def create_user(user: User, request: Request):
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
        IpAddress= request.client.host,
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

# @user.post("/login/")
# async def login(user: User):
#     return conn.execute(users.select().fetchall)
    
# @user.post('/register', status_code=201)
# def register(auth_details: AuthDetails):
#     if any(x['username'] == auth_details.username for x in users):
#         raise HTTPException(status_code=400, detail='Username is taken')
#     hashed_password = auth_handler.get_password_hash(auth_details.password)
#     users.append({
#         'username': auth_details.username,
#         'password': hashed_password    
#     })
#     return
