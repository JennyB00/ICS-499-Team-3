from enum import Enum
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Domain.account import *
from Domain.contacts import *
from Domain.past_chat import *
from Database.database import *
from Database import account_repo, contacts_repo, chat_repo, past_chats_repo
from Service import account_service

# class Status(str, Enum):
#     online = "online"
#     offline = "offline"

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Account])
def read_accounts(limit: int = 100, db: Session = Depends(get_db)):
    return account_repo.get_all_accounts(db, limit)

@router.post("/", response_model=Account)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return account_service.create_account(account, db)

@router.get("/valid_username", response_model=bool)
async def validate_username(username: str, db: Session = Depends(get_db)):
    return account_service.valid_username(username, db)

@router.get("/{username}", response_model=Account)
def read_account(username: str, db: Session = Depends(get_db)):
    db_account = account_repo.get_account(db, username)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.delete("/{username}")
def delete_account(username: str, db: Session = Depends(get_db)):
    if account_repo.delete_account(db,username):
        return {"message": "Account successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Account not found")
    
@router.get("/{username}/password")
def read_account_password(username: str, db: Session = Depends(get_db)):
    db_account = account_repo.get_account(db, username)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account.password

@router.post("/{username}/password")
def update_account_password(username: str, password: str, db: Session = Depends(get_db)):
    if account_repo.update_account_password(db, username, password):
        return {"message": "Password successfully updated"}
    else:
        raise HTTPException(status_code=404, detail="Account not found")

@router.post("/{username}/status")
def update_account_status(username: str, status: Status, db: Session = Depends(get_db)):
    if account_repo.update_account_status(db, username, status):
        return {"message": "Status successfully updated"}
    else:
        raise HTTPException(status_code=404, detail="Account not found")

@router.get("/{username}/contacts", response_model=list[Contact])
def read_account_contacts(username: str, db: Session = Depends(get_db)):
    db_account = account_repo.get_account(db, username)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account.contacts
    # return get_contacts_by_account(db, username)

@router.post("/{username}/contacts", response_model=Contact)
def create_contact_for_account(username: str, contact: str, db: Session = Depends(get_db)):
    if account_repo.get_account(db, username) is None:
        raise HTTPException(status_code=404, detail="Account Not Found")
    if account_repo.get_account(db, contact) is None:
        raise HTTPException(status_code=404, detail="Contact Not Found")
    return contacts_repo.create_contact(db, contact, username)

@router.get("/{username}/past_chats", response_model=list[PastChat])
def read_account_past_chats(username: str, db: Session = Depends(get_db)):
    db_account = account_repo.get_account(db, username)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account.past_chats

@router.post("/{username}/past_chats", response_model=PastChat)
def create_past_chat_for_account(username: str, past_chat_id: int, db: Session = Depends(get_db)):
    if account_repo.get_account(db, username) is None:
        raise HTTPException(status_code=404, detail="Account Not Found")
    elif chat_repo.get_chat(db, past_chat_id) is None:
        raise HTTPException(status_code=404, detail="Chat Not Found")
    else:
        return past_chats_repo.create_past_chat(db, past_chat_id, username)

# @router.delete("/{username}/contacts/{id}")
# def delete_contact_for_account(username: str, id: int, db: Session = Depends(get_db)):
#     if account_repo.get_account(db, username) is None:
#         raise HTTPException(status_code=404, detail="Account not found")
#     if contacts_repo.delete_contact(db, id):
#         return {"message": "Contact Deleted"}
#     else:
#         raise HTTPException(status_code=404, detail="Contact not found")

# @router.delete()
# def delete_past_chat_for_account():
#     pass
