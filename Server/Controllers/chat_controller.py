from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Domain.chat import *
from Domain.privileges import *
from Domain.message import *
from Database.database import *
from Database import chat_repo, privileges_repo, message_repo
from Service import chat_service


router = APIRouter(
    prefix="/chats",
    tags=["chats"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[Chat])
def read_chats(limit: int = 100, db: Session = Depends(get_db)):
    return chat_repo.get_all_chats(db, limit=limit)

@router.post("/", response_model=Chat)
def create_chat(username: str, db: Session = Depends(get_db)):
    return chat_service.create_chat(username, db)

@router.get("/{id}", response_model=Chat)
def read_chat(id: int, db: Session = Depends(get_db)):
    db_chat = chat_repo.get_chat(db, id)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat

@router.delete("/{id}")
def delete_chat(id: int, db: Session = Depends(get_db)):
    if chat_service.delete_chat(id, db):
        return {"message": "Chat successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Chat not found")
    
@router.get("/{id}/users", response_model=list[str])
async def read_chat_users(id: int, db: Session = Depends(get_db)):
    if not chat_repo.get_chat(db, id):
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat_service.get_users_for_chat(id, db)
    
@router.get("/{id}/active", response_model=list[str])
async def read_chat_active_users(id: int, db: Session = Depends(get_db)):
    if not chat_repo.get_chat(db, id):
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat_service.get_active_users_for_chat(id, db)

@router.get("/{id}/privileges", response_model=list[Privileges])
def read_chat_privileges(id: int, db: Session = Depends(get_db)):
    db_chat = chat_repo.get_chat(db, id)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return db_chat.privileges

@router.post("/{id}/privileges", response_model=Privileges)
def create_privileges_for_chat(id: int, privileges: PrivilegesCreate, db: Session = Depends(get_db)):
    if chat_repo.get_chat(db, id) is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    db_privilege = privileges_repo.create_privileges(db, privileges, id)
    return db_privilege

@router.get("/{id}/messages", response_model=list[Message])
def read_chat_messages(id: int,
                       username: str | None = None,
                       date: datetime | None = None,
                       word: str | None = None,
                       db: Session = Depends(get_db)):
    db_chat = chat_repo.get_chat(db, id)
    if db_chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    elif username:
        # validate username?
        return chat_service.search_by_username_for_chat(id, username, db)
    elif date:
        return chat_service.search_by_date_for_chat(id, date, db)
    elif word:
        return chat_service.search_by_word_for_chat(id, word, db)
    else:
        return db_chat.messages

@router.post("/{id}/messages", response_model=Message)
def create_message_for_chat(id: int, message: MessageCreate, db: Session = Depends(get_db)):
    if chat_repo.get_chat(db, id) is None:
        raise HTTPException(status_code=404, detail="Chat not found")
    return message_repo.create_message(db, message, id)

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