from sqlalchemy.orm import Session
from .models import PastChatModel

def get_past_chat(db: Session, id: int) -> (PastChatModel | None):
    return db.query(PastChatModel).filter(PastChatModel.id == id).first()

def create_past_chat(db: Session, chat_id: int, user: str) -> (PastChatModel):
    db_message = PastChatModel(username=user, past_chat_id=chat_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def delete_past_chat(db: Session, id: int) -> bool:
    db_past_chat = get_past_chat(db, id)
    if db_past_chat is None:
        return False
    else:
        db.delete(db_past_chat)
        db.commit()
        return True