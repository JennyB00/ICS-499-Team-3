from datetime import datetime
from Domain.chat import *
from Database.database import *
from sqlalchemy.orm import Session
from Database.models import *
from Database import chat_repo as cr
from Domain.privileges import *

def get_privileges_for_user_in_chat(chat_id: int, username: str, db: Session) -> Privileges:
    db_chat = cr.get_chat(db, chat_id)
    privileges = None
    for p in db_chat.privileges:
        if p.username is username:
            privileges = p
    if privileges is None:
        return None
    return Privileges.from_orm(privileges)

def get_chats_by_ids(chat_ids: list[int], db: Session) -> list[Chat]:
    chats = []
    for id in chat_ids:
        db_chat = cr.get_chat(db, id)
        if db_chat != None:
            chats.append(Chat.from_orm(db_chat))
    return chats

# Get chat -> get privilegs -> list of past users -> filter those online status
def get_active_users_for_chat(chat_id: int, db: Session) -> list[str]:
    pass

def search_by_date_for_chat(chat_id: int, date: datetime, db: Session) -> list[Message]:
    pass

def search_by_username_for_chat(chat_id: int, username: str, db: Session) -> list[Message]:
    pass

def search_by_word_for_chat(chat_id: int, search: str, db: Session) -> list[Message]:
    pass