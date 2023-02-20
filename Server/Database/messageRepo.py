from sqlalchemy.orm import Session
from .models import MessageModel
from Domain.message import *

def get_all_messages(db: Session, limit: int = 100) -> list[MessageModel]:
    return db.query(MessageModel).limit(limit).all()

def get_message(db: Session, id: int):
    return db.query(MessageModel).filter(MessageModel.id == id).first()

def create_message(db: Session, message: MessageCreate, chat_id: int):
    db_message = MessageModel(**message.dict(), chat_id=chat_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
