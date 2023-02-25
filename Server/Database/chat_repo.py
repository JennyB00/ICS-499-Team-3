from sqlalchemy.orm import Session
from .models import ChatModel, PrivilegesModel, MessageModel
from Domain.chat import Chat

def get_all_chats(db: Session, limit: int = 100) -> list[ChatModel]:
    return db.query(ChatModel).limit(limit).all()

def get_chat(db: Session, id: int) -> (ChatModel | None):
    return db.query(ChatModel).filter(ChatModel.id == id).first()

def get_privileges_by_chat(db: Session, chat_id: int) -> list[PrivilegesModel]:
    db_chat = get_chat(db, chat_id)
    if db_chat is None:
        return []
    else:
        return db_chat.privileges

def get_messages_by_chat(db: Session, chat_id: int) -> list[MessageModel]:
    db_chat = get_chat(db, chat_id)
    if db_chat is None:
        return []
    else:
        return db_chat.messages

def create_chat(db: Session) -> ChatModel:
    db_chat = ChatModel()
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

# def create_chat_privileges(db: Session, privileges: Privil):
#     return

# def create_chat_message(db: Session):
#     return