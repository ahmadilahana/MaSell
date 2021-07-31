from component.util import EmailValid, PasswordValid, RealStr, realPhone
from typing import List, Optional
from fastapi.param_functions import Depends
from fastapi.params import Query
import phonenumbers
from pydantic import BaseModel
from pydantic.fields import Field
from datetime import datetime
from fastapi import Request, Security
from phonenumbers import PhoneNumber
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
import re
from sqlalchemy.sql.expression import false

class User(BaseModel):
    firsName: RealStr = None
    lastName: RealStr = None
    email: EmailValid = None
    avatarUrl: RealStr = None
    countryId: int = None
    countryCode: RealStr = None
    country: RealStr = None
    verifyCode: int = None
    registerAt: int = None
    deviceId: int = None
    isActived: int = None
    password: PasswordValid = None
    phone: realPhone = None#Field(None, max_length=15, regex="^[-+]?[0-9]+$" )


class Login(BaseModel):
    email: EmailValid = None,
    password: PasswordValid = None