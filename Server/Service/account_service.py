from sqlalchemy.orm import Session
from fastapi import Depends
from Database.database import *
from Database import account_repo as ar
from Domain.account import Account

# accounts = ar.get_all_accounts(Depends(get_db),None)

def login_user(username: str, password: str, db: Session) -> bool:
    db_account = ar.get_account(db, username)
    if password is db_account.password:
        db_account.status = "online"
        db.commit()
        db.refresh(db_account)
        return True
    else:
        return False

def logout_user(username: str, db: Session) -> None:
    db_account = ar.get_account(db, username)
    db_account.status = "offline"
    db.commit()
    db.refresh(db_account)

# def get_account_by_username(username: str, db: Session) -> (Account | None):
#     return ar.get_account(db,username)

def get_accounts_by_usernames(usernames: list[str], db: Session) -> list[Account]:
    pass

# def valid_username(username: str, db: Session) -> bool:
#     if username in ar.get_all_usernames(db):
#         return False
#     else:
#         return True