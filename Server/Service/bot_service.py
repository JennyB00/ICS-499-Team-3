from Domain.bot import Bot
from Database import account_repo
from sqlalchemy.orm import Session
from Database.models import *

def get_session_id_by_username(username: str, db: Session) -> str:
    db_account = account_repo.get_account(db, username)
    if not db_account:
        return ""
    return db_account.username
