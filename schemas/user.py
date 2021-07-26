from pydantic import BaseModel

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
    IpAddress: str
    isActived: int
    password: str