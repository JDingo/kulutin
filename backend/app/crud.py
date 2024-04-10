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


def get_categories(db: Session):
    return db.query(models.Category).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(category_name=category.category_name)

    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
