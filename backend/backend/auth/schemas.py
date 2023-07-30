# from pydantic import BaseModel


# class GroupBase(BaseModel):
#     name: str


# class GroupCreate(GroupBase):
#     pass


# class Group(GroupBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     groups: list[Group] = []

#     class Config:
#         orm_mode = True


from uuid import UUID
from pydantic import BaseModel, Field, model_validator

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    
    
class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserAuth(BaseModel, validate_assignment=True):
    email: str = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")
    repeat_password: str = Field(..., min_length=5, max_length=24, description="user repeat password")

    @model_validator(mode="before")
    @classmethod
    def validate_passwords(cls, values):
        if values["password"] != values["repeat_password"]:
            raise ValueError("passwords do not match")
        return values
    

class UserOut(BaseModel):
    id: UUID
    email: str


class SystemUser(UserOut):
    password: str