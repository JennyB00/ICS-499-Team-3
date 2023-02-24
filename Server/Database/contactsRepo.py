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

def create_contact(db: Session, contact: ContactCreate) -> ContactModel:
    db_contact = ContactModel(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact