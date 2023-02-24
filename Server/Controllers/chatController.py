from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Domain.chat import *
from Domain.privileges import Privileges
from Domain.history import History
from Domain.message import *
from Database.Database import *
from Database import chatRepo
from Database.privilegesRepo import *
from Database.messageRepo import *

router = APIRouter(
    prefix="/chats",
    tags=["chats"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Chat])
def read_chats(limit: int = 100, db: Session = Depends(get_db)):
    return chatRepo.get_all_chats(db, limit=limit)

@router.get("/{chat_id}", response_model=Chat)
def read_chat(chat_id: int, db: Session = Depends(get_db)):
    return chatRepo.get_chat(db, chat_id)

@router.get("/{chat_id}/privileges", response_model=list[Privileges])
def read_chat_privileges(chat_id: int, db: Session = Depends(get_db)):
    return chatRepo.get_privileges_by_chat(db, chat_id)

@router.get("/{chat_id}/messages", response_model=list[Message])
def read_chat_messages(chat_id: int, db: Session = Depends(get_db)):
    return chatRepo.get_messages_by_chat(db, chat_id)

@router.post("/", response_model=Chat)
def create_chat(db: Session = Depends(get_db)):
    return chatRepo.create_chat(db)

@router.post("/{chat_id}/privileges", response_model=Privileges)
def create_privileges_for_chat(chat_id: int, privileges: PrivilegesCreate, db: Session = Depends(get_db)):
    db_privilege = create_privileges(db, privileges, chat_id)
    return db_privilege

@router.post("/{chat_id}/messages", response_model=Message)
def create_message_for_chat(chat_id: int, message: MessageCreate, db: Session = Depends(get_db)):
    return create_message(db, message, chat_id)