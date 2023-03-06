from sqlalchemy.orm import Session
from fastapi import Depends
from Database.database import *
from Database import account_repo as ar

# accounts = ar.get_all_accounts(Depends(get_db),None)

def login_user(username: str, password: str, db: Session = Depends(get_db)) -> bool:
    db_account = ar.get_account(db, username)
    if password is db_account.password:
        db_account.status = "online"
        db.commit()
        db.refresh(db_account)
        return True
    else:
        return False

def logout_user(username: str, db: Session = Depends(get_db)) -> None:
    db_account = ar.get_account(db, username)
    db_account.status = "offline"
    db.commit()
    db.refresh(db_account)
