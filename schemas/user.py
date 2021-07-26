from pydantic import BaseModel
from datetime import datetime
from fastapi import Request



class User(BaseModel):
    firsName: str
    lastName: str
    email: str
    avatarUrl: str
    countryId: int
    countryCode: str
    country: str
    verifyCode: int
    registerAt: int
    deviceId: int
    isActived: int
    password: str