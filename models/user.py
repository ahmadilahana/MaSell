from sqlalchemy import Table,Column,Integer,String
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import SmallInteger
from config.db import meta

users = Table(
    'users',meta,
    Column('userId', Integer,primary_key=True),
    Column('firsName', String(255)),
    Column('lastName', String(255)),
    Column('email', String(255)),
    Column('avatarUrl', String(255)),
    Column('countryId', SmallInteger),
    Column('countryCode', String(5)),
    Column('country', String(255)),
    Column('verifyCode', SmallInteger),
    Column('registerAt', SmallInteger),
    Column('deviceId', SmallInteger),
    Column('IpAddress', String(255)),
    Column('isActived', SmallInteger),
    Column('password', String(255)),
    Column('phone', String(15)),
)