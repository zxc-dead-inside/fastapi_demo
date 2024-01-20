import re

from pydantic import BaseModel, constr, validator


class UserData(BaseModel):
    phone: constr(strict=True)
    address: str

    @validator("phone")
    def validate_phone(cls, value):
        phone_regex = r"^(?:'\+?\d{11}'|\+?\d{11})$"
        if not re.match(phone_regex, value):
            raise ValueError("Invalid phone number format")
        value = value.strip("'\"")
        return '+7' + value[1:] if value.startswith('8') else value
