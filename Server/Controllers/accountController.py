from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from Domain.account import *
from Database.Database import *
from Database.accountRepo import *
from Database.contactsRepo import *

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[AccountBase])
def read_accounts(limit: int = 100, db: Session = Depends(get_db)):
    return get_all_accounts(db, limit)

@router.get("/{username}", response_model=AccountPy)
def read_account(username: str, db: Session = Depends(get_db)):
    db_account = get_account(db, username)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return AccountPy.from_orm(db_account)

@router.get("/{username}/contacts", response_model=list[AccountPy])
def read_account_contacts(username: str, db: Session = Depends(get_db)):
    return get_contacts_by_account(db, username)

@router.post("/", response_model=AccountPy)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account(db, account)

@router.post("/{username}/contacts", response_model=ContactPy)
def create_contact_for_account(username: str, contact: ContactCreate,db: Session = Depends(get_db)):
    return create_contact(db, contact, username)