from typing import List
from fastapi import FastAPI, Query, HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) #creates all tables
app = FastAPI(
    title="databricks-table-crud-fastapi",
    description="This demo application demonstrates an implementation for basic CRUD operations on a databricks table via a REST Api.",
    version="0.1.0"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/customer", tags=["customer"], response_model=List[schemas.Customer])
def get_customers(
    country: models.Country = None,
    car: models.Car = None,
    active: bool = None,
    age: int = None,
    db: Session = Depends(get_db)
):
    db_customers = crud.get_customers(db, country, car, active, age)
    return db_customers


@app.get("/customer/{id}", tags=["customer"], response_model= schemas.Customer)
def get_customer(id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, id)
    return db_customer    


@app.post("/customer", tags=["customer"], response_model= schemas.Customer)
def create_customer(customer: schemas.Customer, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, customer.Id)
    if db_customer:
        raise HTTPException(status_code=400, detail=f"A customer with the id '{customer.Id}' already exists.")
    
    db_customer = crud.create_customer(db, customer)
    return db_customer       


@app.patch("/customer/{id}", tags=["customer"], response_model= schemas.Customer)
def update_customer(id: int, customer: schemas.UpdateCustomer, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail=f"A customer with the id '{id}' does not exist.")
    
    db_customer = crud.update_customer(db, id, customer)
    return db_customer    


@app.delete("/customer/{id}", tags=["customer"], response_model= schemas.Customer)
def delete_customer(id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail=f"A customer with the id '{id}' does not exist.")

    db_customer = crud.delete_customer(db, id)
    return db_customer   