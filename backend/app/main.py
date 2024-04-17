from os import environ
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [environ.get("FRONTEND_URL")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_home():
    return {"message": "Hello World"}


@app.get("/transactions", response_model=list[schemas.Transaction])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_transactions(db, skip, limit)


@app.get("/transactions/{transaction_id}", response_model=schemas.Transaction)
def read_transcation(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = crud.get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction


@app.get("/transactions/category/{category_id}", response_model=schemas.Transaction)
def read_transactions_by_category(category_id: int, db: Session = Depends(get_db)):
    db_transactions_by_category = crud.get_transactions_by_category(
        db, category_id=category_id
    )
    if db_transactions_by_category is None:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return db_transactions_by_category


@app.post("/transactions", response_model=schemas.Transaction)
def create_transaction(
    transaction: schemas.TransactionCreate, db: Session = Depends(get_db)
):
    return crud.create_transaction(db, transaction)


@app.delete("/transactions/{id}", response_model=schemas.Transaction)
def delete_transaction(
    id: int, transaction: schemas.Transaction, db: Session = Depends(get_db)
):
    return crud.delete_transaction(db, transaction, id)


@app.put("/transactions/{id}", response_model=schemas.Transaction)
def update_transaction(
    id: int, transaction: schemas.Transaction, db: Session = Depends(get_db)
):
    return crud.update_transaction(db, transaction, id)


@app.get("/categories", response_model=list[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@app.post("/categories", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category=category)
