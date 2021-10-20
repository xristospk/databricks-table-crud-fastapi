from sqlalchemy import schema
from sql_app import schemas
from typing import List
from sqlalchemy.orm import Session
from . import models


def get_customer(db: Session, customerId: int):
    return db.query(models.Customer).filter(models.Customer.Id == customerId).first()


def get_customers(db: Session, filter_country: models.Country = None, filter_car: models.Car = None, filter_active: bool = None, filter_age: int = None):
    query = db.query(models.Customer)

    if filter_country is not None:
        query = query.filter(models.Customer.Country == filter_country.value)
    
    if filter_car is not None:
        query = query.filter(models.Customer.Car == filter_car.value)
    
    if filter_active is not None:
        query = query.filter(models.Customer.Active == filter_active)    
    
    if filter_age is not None:
        query = query.filter(models.Customer.Age == filter_age)    

    return query.all()


def create_customer(db: Session, customer: schemas.Customer):
    db_item = models.Customer(**customer.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item         


def update_customer(db: Session, customerId: int, customer: schemas.UpdateCustomer):
    db_item = db.query(models.Customer).get(customerId)
    update_data = customer.dict(exclude_unset=True)
   
    for key, value in update_data.items():
        setattr(db_item, key, value)

    db.add(db_item)
    db.commit()
    return db_item


def delete_customer(db:Session, customerId: int):
    db_item = db.query(models.Customer).get(customerId)
    db.delete(db_item)
    db.commit()
    return db_item
