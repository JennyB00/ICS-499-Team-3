from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Domain.chat import *
from Domain.privileges import *
from Domain.history import History
from Domain.message import *
from Database.database import *
from Database import chat_repo, privileges_repo, message_repo
from Domain.message import *


router = APIRouter(
    prefix="/chats",
    tags=["chats"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[Chat])
def read_chats(limit: int = 100, db: Session = Depends(get_db)):
    return chat_repo.get_all_chats(db, limit=limit)

@router.get("/{chat_id}", response_model=Chat)
def read_chat(chat_id: int, db: Session = Depends(get_db)):
    db_chat = chat_repo.get_chat(db, chat_id)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat

@router.get("/{chat_id}/privileges", response_model=list[Privileges])
def read_chat_privileges(chat_id: int, db: Session = Depends(get_db)):
    db_chat = chat_repo.get_chat(db, chat_id)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat.privileges

@router.get("/{chat_id}/messages", response_model=list[Message])
def read_chat_messages(chat_id: int, db: Session = Depends(get_db)):
    db_chat = chat_repo.get_chat(db, chat_id)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat.history

@router.post("/", response_model=Chat)
def create_chat(db: Session = Depends(get_db)):
    return chat_repo.create_chat(db)

@router.post("/{chat_id}/privileges", response_model=Privileges)
def create_privileges_for_chat(chat_id: int, privileges: PrivilegesCreate, db: Session = Depends(get_db)):
    if chat_repo.get_chat(db, chat_id) is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    db_privilege = privileges_repo.create_privileges(db, privileges, chat_id)
    return db_privilege

@router.post("/{chat_id}/messages", response_model=Message)
def create_message_for_chat(chat_id: int, message: MessageCreate, db: Session = Depends(get_db)):
    if chat_repo.get_chat(db, chat_id) is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return message_repo.create_message(db, message, chat_id)


@router.delete("/{chat_id}")
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
    return chat_repo.delete_chat(db, chat_id)

# @router.delete("/{chat_id}/privileges/{p_id}")
# def delete_privilege_for_chat(chat_id: int, p_id: int, db: Session = Depends(get_db)):
#     if chat_repo.get_chat(db, chat_id) is None:
#         raise HTTPException(status_code=404, detail="Chat not found")
#     return privileges_repo.delete_privileges(db, p_id)

# @router.delete("/{chat_id}/messages/{m_id}")
# def delete_message_for_chat(chat_id: int, m_id: int, db: Session = Depends(get_db)):
#     if chat_repo.get_chat(db, chat_id) is None:
#         raise HTTPException(status_code=404, detail="Chat not found")
#     return message_repo.delete_message(db, m_id)