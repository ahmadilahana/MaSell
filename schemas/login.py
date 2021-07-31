from pydantic import BaseModel
from sqlalchemy.sql.expression import true
from models.main import users
from config.db import conn


class loginUser(BaseModel):
    email: str
    password: str

class validationLogin(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v): 
        cekDb = conn.execute(users.select().where(users.c.email == v)).fetchall()
        emails= cekDb[0].email
        if emails == v:
            return False
        else:
            return True