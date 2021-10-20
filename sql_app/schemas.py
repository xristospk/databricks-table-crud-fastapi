from typing import Optional
from pydantic import BaseModel
from datetime import date
from .models import Country, Car, FavoriteFood

class Customer(BaseModel):
    Id: int
    Name: str
    Email: str
    Country: Country
    Car: Car
    FavoriteFood: FavoriteFood
    Registered: date
    Active: bool
    Age: int
    
    class Config:
        orm_mode = True

class UpdateCustomer(BaseModel):
    Name: Optional[str]
    Email: Optional[str]
    Country: Optional[Country]
    Car: Optional[Car]
    FavoriteFood: Optional[FavoriteFood]
    Registered: Optional[date]
    Active: Optional[bool]
    Age: Optional[int]      