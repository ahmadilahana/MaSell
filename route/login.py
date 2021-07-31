from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.logger import logger
from fastapi.routing import APIRouter
from sqlalchemy.sql.expression import select
from starlette.requests import Request
from models.auth import AuthHandler
from schemas.user import User
from schemas.login import loginUser, validationLogin
from config.db import conn
from models.main import users


login = APIRouter()
auth = AuthHandler()
# emailCon = conn.execute("SELECT email FROM users")


# @login.post('/register', status_code=201)
# def register(user: User, request: Request):
#     if any(email == user.email for email in user):
#         raise HTTPException(status_code=400, detail='Email is taken')
#     hashed_password = auth.get_password_hash(user.password)
#     return conn.execute(users.insert().values(
            # firsName= user.firsName,
            # lastName= user.lastName,
            # email= user.email,
            # avatarUrl= user.avatarUrl,
            # countryId= user.countryId,
            # countryCode= user.countryCode,
            # country= user.country,
            # verifyCode= user.verifyCode,
            # registerAt= user.registerAt,
            # deviceId= user.deviceId,
            # IpAddress= request.client.host,
            # isActived= user.isActived,
            # password= hashed_password,
            # phone= user.phone
#         ))

@login.post("/resgister")
def register(user: User, request: Request):
    userOnDb = conn.execute(users.select()).fetchall()
    if any(x['email'] == user.email for x in userOnDb):
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth.get_password_hash(user.password)
    conn.execute(users.insert().values(
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
        password= hashed_password,
        phone= user.phone
    ))
    # userOnDb.append({
    #     'firsName': user.firsName,
    #     'lastName': user.lastName,
    #     'email': user.email,
    #     'avatarUrl': user.avatarUrl,
    #     'countryId': user.countryId,
    #     'countryCode': user.countryCode,
    #     'country': user.country,
    #     'verifyCode': user.verifyCode,
    #     'registerAt': user.registerAt,
    #     'deviceId': user.deviceId,
    #     'IpAddress': request.client.host,
    #     'isActived': user.isActived,
    #     'password': hashed_password,
    #     'phone': user.phone    
    # })



@login.post('/login')
def login_app(loginn: loginUser):
    validEmail = conn.execute(users.select().where(users.c.email == loginn.email)).fetchall()
    if validEmail[0].email == loginn.email and validEmail[0].password == loginn.password:
        token = auth.encode_token(loginn.email, loginn.password)
        return { 'token': token }
    else:
        raise HTTPException(status_code=400, detail='Email atau Password Salah')

# @login.get('/unprotected')
# def unprotected():
#     return { 'hello': 'world' }


@login.get('/home')
def protected(email=Depends(auth.auth_wrapper)):
    return { 'name': email }