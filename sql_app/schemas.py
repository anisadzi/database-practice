from typing import Union

from pydantic import BaseModel


# initial schemas
class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

# initial schemas
class ItemCreate(ItemBase):
    pass

# schemas for reading/returning
class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# initial schemas
class UserBase(BaseModel):
    email: str

# initial schemas
class UserCreate(UserBase):
    password: str

# schemas for reading/returning
class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True