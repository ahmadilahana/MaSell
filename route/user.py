from component.util import EmailValid, PasswordValid
from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from sqlalchemy.sql.expression import false
from schemas.user import RealStr, User, realPhone, Login
from config.db import conn
from models.main import users
from fastapi.security import OAuth2PasswordBearer

user = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@user.get("/")
async def read_user():
    return "UHUY"

@user.get("/users/{userId}")
async def read_user_by_id(userId: RealStr):
    return conn.execute(users.select().where(users.c.userId == userId)).fetchall()

@user.get("/users/getId/")
async def coba(login: PasswordValid):
    return login

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
        password= user.password,
        phone= user.phone
    ))
    
@user.put("/users/update{userId}")
async def update_user(userId: int, user: User):
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
        password= user.password,
        phone= user.phone
    ).where(users.c.userId == userId))
    return conn.execute(users.select()).fetchall()


@user.delete("/users/delete/{userId}")
async def delete_by_id(userId: int):
    conn.execute(users.delete().where(users.c.userId == userId))
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
