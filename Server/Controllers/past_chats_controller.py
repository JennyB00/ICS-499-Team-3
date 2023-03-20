from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Domain.contacts import *
from Database.database import *
from Database import past_chats_repo as pr

router = APIRouter(
    prefix="/past_chats",
    tags=["past_chats"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}", response_model=int)
def read_past_chat(id: int, db: Session = Depends(get_db)):
    db_past_chat = pr.get_past_chat(db, id)
    if db_past_chat is None:
        raise HTTPException(status_code=404, detail="Past Chat not found")
    return db_past_chat.past_chat_id

@router.delete("/{id}")
def delete_past_chat(id: int, db: Session = Depends(get_db)):
    if pr.delete_past_chat(db, id):
        return {"message":"Past Chat successfully deleted"}
    else:
        raise HTTPException(status_code=404,detail="Past Chat not found")