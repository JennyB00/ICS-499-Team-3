from sqlalchemy.orm import Session
from Database.database import *
from Database import account_repo as ar
from Domain.account import *

# accounts = ar.get_all_accounts(Depends(get_db),None)

# def get_account_by_username(username: str, db: Session) -> (Account | None):
#     return ar.get_account(db,username)

def get_accounts_by_usernames(usernames: list[str], db: Session) -> list[Account]:
    accounts = []
    for u in usernames:
        accounts.append(Account.from_orm(ar.get_account(db, u)))
    return accounts

#business logic for joining site
def create_account(account: AccountCreate, db: Session) -> Account:
    # account.password = hashlib.sha256(account.password.encode()).hexdigest()
    db_account = ar.create_account(db, account)
    account = Account.from_orm(db_account)
    return account

def valid_username(username: str, db: Session) -> bool:
    if username in ar.get_all_usernames(db):
        return False
    else:
        return True