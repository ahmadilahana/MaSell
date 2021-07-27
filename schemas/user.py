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

class RealStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v): 
               
        if type(v) != str:            
            try:
                if type(v) == float:
                    v = str(int(v))
                else:
                    v = str(v)
                
            except:
                raise ValueError("Not a valid String")    
        if not isinstance(v, str):
            raise ValueError("Not a valid String")
        if not v:
            return str(v)
            
        if bool(re.compile('^[a-zA-Z\d\.\,\&\-\_\()\'\\/@\s]+$').match(v)):
            return str(v)
        else:
            print(v)
            raise ValueError(str(v) + "unallowed character")


def ValidPhoneNumber(phone_number: RealStr):
    my_number = phonenumbers.parse(phone_number, "ID")
    validPhone = phonenumbers.is_valid_number(my_number)
    
    if not validPhone:
        return false

    if 7 < len(phone_number) < 14:
        rule = re.compile(r'^(?:\+?44)?[07]\d{9,13}$')
        if not rule.search(phone_number):            
            return false
        else:
            return phone_number.isnumeric()
    else:
        return false

class User(BaseModel):
    firsName: RealStr = None
    lastName: RealStr = None
    email: RealStr = None
    avatarUrl: RealStr = None
    countryId: int = None
    countryCode: RealStr = None
    country: RealStr = None
    verifyCode: int = None
    registerAt: int = None
    deviceId: int = None
    isActived: int = None
    password: str = None
    phone: RealStr = None#Field(None, max_length=15, regex="^[-+]?[0-9]+$" )