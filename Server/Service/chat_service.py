from datetime import datetime
from Domain.chat import *
from Domain.privileges import *
from Domain.account import *
from sqlalchemy.orm import Session
from Database.models import *
from Database import chat_repo as cr, privileges_repo as pr, account_repo as ar

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
    db_chat = cr.get_chat(db, chat_id)
    users = []
    for p in db_chat.privileges:
        users.append(p.username)
    for u in users:
        user = ar.get_account(db, u)
        if user.status == Status.offline:
            users.remove(u)
    return users

def create_chat(username: str, db: Session) -> ChatModel:
    db_chat = cr.create_chat(db)
    privileges = PrivilegesCreate(username=username,
                                  send=True,
                                  recieve=True,
                                  add_user=True,
                                  delete_message=True,
                                  delete_chat=True)
    pr.create_privileges(db,privileges,db_chat.id)
    return db_chat

def search_by_date_for_chat(chat_id: int, date: datetime, db: Session) -> list[Message]:
    db_messages = cr.get_messages_by_chat(db, chat_id)
    messages = []
    for m in db_messages:
        if m.date == date:
            messages.append(Message.from_orm(m))
    return messages

def search_by_username_for_chat(chat_id: int, username: str, db: Session) -> list[Message]:
    db_messages = cr.get_messages_by_chat(db, chat_id)
    messages = []
    for m in db_messages:
        if m.username == username:
            messages.append(Message.from_orm(m))
    return messages

def search_by_word_for_chat(chat_id: int, search: str, db: Session) -> list[Message]:
    db_messages = cr.get_messages_by_chat(db, chat_id)
    messages = []
    for m in db_messages:
        if m.type == "str":
            messages.append(m)
    filtered_messages = []
    for m in messages:
        #Needs to change. Not sure how to convert LargeBinary to String
        message = m.message
        words = message.split()
        for w in words:
            if w == search:
                filtered_messages.append(m)
    return filtered_messages