from fastapi.exceptions import HTTPException
import phonenumbers
from phonenumbers import PhoneNumber
import re

regexEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,5}$'

class realPhone(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v): 
        phonnInt = ValidPhoneNumber(v)
        
        if phonnInt != False:
            return str(v)
        else:
            # print(v)
            raise ValueError("Not a valid Phone")

class EmailValid(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v): 
        phonnInt = ValidateEmail(v)
        if phonnInt != False:
            return str(v)
        else:
            # print(v)
            raise ValueError("Not a valid Email")


class PasswordValid(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v): 
        phonnInt = ValidPassword(v)
        if phonnInt != False:
            return str(v)
        else:
            # print(v)
            raise ValueError("Not a valid Password")

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


def ValidPhoneNumber(phone_number: str):
    phoneFormat = format(int(phone_number[:-1]), ",").replace(",", "-") + phone_number[-1]
    my_number = phonenumbers.parse(phoneFormat, "ID")
    validPhone = phonenumbers.is_valid_number(my_number)
    if not validPhone:
        return False

    if 7 < len(phone_number) < 14:
        return phone_number.isnumeric()
    else:
        return False


def ValidateEmail(email: str):
    if re.search(regexEmail, email):
        return True
    else:
        return False

def ValidPassword(pwd: str):
    if 5 < len(pwd) < 21:
        return True
    else:
        raise HTTPException(status_code=400,detail="Password length between 6 - 20")