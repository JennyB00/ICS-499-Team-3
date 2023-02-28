# import mysql.connector
# class ContactsRepo:
#     def get_all_contacts(cursor: mysql.connector.connection.MySQLCursor):
#         query = ("SELECT * FROM contacts")
#         cursor.execute(query)
#         results = []
#         for (username, contact) in cursor:
#             results.append({"Username":username})
# 	    results.append({"Contact":contact})
#         return results

from sqlalchemy.orm import Session
from .models import ContactModel
from Domain.contacts import *

def create_contact(db: Session, contact: str, owner: str) -> ContactModel:
    db_contact = ContactModel(contact=contact, owner_id=owner)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contact(db: Session, id: int) -> (ContactModel | None):
    return db.query(ContactModel).filter(ContactModel.id == id).first()

def delete_contact(db: Session, id: int) -> bool:
    db_contact = get_contact(db, id)
    if db_contact is None:
        return False
    db.delete(db_contact)
    db.commit()
    return True