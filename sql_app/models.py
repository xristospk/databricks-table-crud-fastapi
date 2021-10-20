from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
import enum
from .database import Base

class Country(str, enum.Enum):
    Germany = "Germany"
    France = "France"

class FavoriteFood(str, enum.Enum):
    Sandwiches = "sandwiches"
    Soups = "soups"
    Salads = "salads"
    Pasta = "pasta"    

class Car(str, enum.Enum):
    MB = "Mercedes-Benz"
    VW = "Volkswagen"
    BMW = "BMW"

class Customer(Base):
    __tablename__ = "Customer"

    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Email = Column(String)
    Country = Column(String) #Enum(Country)
    Car = Column(String) #Enum(Car)
    FavoriteFood = Column(String) #Enum(FavoriteFood)
    Registered = Column(Date)
    Active = Column(Boolean)
    Age = Column(Integer) 