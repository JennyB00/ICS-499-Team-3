from sqlalchemy.orm import Session
from .models import AccountModel
from Domain.account import *
import uuid


def get_all_accounts(db: Session, limit: (int | None) = 100) -> list[AccountModel]:
    return db.query(AccountModel).limit(limit).all()

def get_all_usernames(db: Session, limit: (int | None) = None) -> list[str]:
    accounts = db.query(AccountModel).all()
    names = []
    for a in accounts:
        names.append(a.username)
    return names

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

def update_account_password(db: Session, username: str, password: str) -> bool:
    db_account = get_account(db, username)
    if db_account is None:
        return False
    db_account.password = password
    db.commit()
    db.refresh(db_account)
    return True

def update_account_status(db: Session, username: str, status: Status) -> bool:
    db_account = get_account(db, username)
    if db_account is None:
        return False
    db_account.status = status
    db.commit()
    db.refresh(db_account)
    return True

def delete_account(db: Session, username: str) -> bool:
    db_account = get_account(db, username)
    if db_account is None:
        return False
    else:
        db.delete(db_account)
        db.commit()
        return True
    # db.query(AccountModel).filter(AccountModel.username == account).delete()
    
