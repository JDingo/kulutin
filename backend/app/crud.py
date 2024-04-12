from http.client import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from . import models, schemas


def get_transactions(
    db: Session,
    skip: int,
    limit: int,
):
    return db.query(models.Transaction).offset(skip).limit(limit).all()


def get_transaction(db: Session, transaction_id: int):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.id == transaction_id)
        .first()
    )


def get_transactions_by_category(db: Session, category_id: int):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.category_id == category_id)
        .first()
    )


def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(
        merchant=transaction.merchant,
        date=transaction.date,
        total=transaction.total,
        category_id=transaction.category_id if transaction.category_id else 0,
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def delete_transaction(db: Session, transcation: schemas.Transaction, id):
    db.query(models.Transaction).filter(models.Transaction.id == id).delete()
    db.commit()
    return transcation


def update_transaction(db: Session, transaction: schemas.Transaction, id):
    db_transaction_query = db.query(models.Transaction).filter(
        models.Transaction.id == id
    )
    db_transaction = db_transaction_query.first()

    if db_transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with {id} not found",
        )

    db_transaction.merchant = transaction.merchant
    db_transaction.date = transaction.date
    db_transaction.total = transaction.total
    db_transaction.category_id = transaction.category_id

    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def get_categories(db: Session):
    return db.query(models.Category).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(category_name=category.category_name)

    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
