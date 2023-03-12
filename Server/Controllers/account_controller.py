from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Domain.account import *
from Domain.contacts import *
from Domain.past_chat import *
from Database.database import *
from Database import account_repo, contacts_repo, chat_repo, past_chats_repo

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Account])
def read_accounts(limit: int = 100, db: Session = Depends(get_db)):
    return account_repo.get_all_accounts(db, limit)

@router.get("/{username}", response_model=Account)
def read_account(username: str, db: Session = Depends(get_db)):
    db_account = account_repo.get_account(db, username)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.get("/{username}/contacts", response_model=list[Contact])
def read_account_contacts(username: str, db: Session = Depends(get_db)):
    db_account = account_repo.get_account(db, username)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account.contacts
    # return get_contacts_by_account(db, username)

@router.get("/{username}/past_chats", response_model=list[PastChat])
def read_account_past_chats(username: str, db: Session = Depends(get_db)):
    db_account = account_repo.get_account(db, username)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account.past_chats

@router.post("/", response_model=Account)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account(db, account)

@router.post("/{username}/contacts", response_model=Contact)
def create_contact_for_account(username: str, contact: str, db: Session = Depends(get_db)):
    if account_repo.get_account(db, username) is None:
        raise HTTPException(status_code=404, detail="Account Not Found")
    if account_repo.get_account(db, contact) is None:
        raise HTTPException(status_code=404, detail="Contact Not Found")
    return contacts_repo.create_contact(db, contact, username)

@router.post("/{username}/past_chats")
def create_past_chat_for_account(username: str, past_chat_id: int, db: Session = Depends(get_db)):
    if account_repo.get_account(db, username) is None:
        raise HTTPException(status_code=404, detail="Account Not Found")
    if chat_repo.get_chat(db, past_chat_id) is None:
        raise HTTPException(status_code=404, detail="Chat Not Found")
    else:
        past_chats_repo.create_past_chat(db, past_chat_id, username)
        return {"message":"Chat Added"}

@router.delete("/{username}", response_model=bool)
def delete_account(username: str, db: Session = Depends(get_db)):
    if account_repo.delete_account(db,username):
        return {"message": "Account Deleted"}
    else:
        raise HTTPException(status_code=404, detail="Account not found")

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
