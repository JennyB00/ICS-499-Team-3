from sqlalchemy.orm import Session
from .models import AccountModel
from Domain.account import *


def get_all_accounts(db: Session, limit: (int | None) = 100) -> list[AccountModel]:
    return db.query(AccountModel).limit(limit).all()

def get_account(db: Session, username: str) -> (AccountModel | None):
    return db.query(AccountModel).filter(AccountModel.username == username).first()

# def get_contacts_by_account(db: Session, username: str) -> list[str]:
#     db_account = get_account(db, username)
#     if db_account is None:
#         return []
#     else:
#         return db_accou nt.contacts

def create_account(db: Session, account: AccountCreate) -> AccountModel:
    db_account = AccountModel(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def delete_account(db: Session, username: str) -> bool:
    db_account = get_account(db, username)
    if db_account is None:
        return False
    else:
        db.delete(db_account)
        db.commit()
        return True
    # db.query(AccountModel).filter(AccountModel.username == account).delete()
    
