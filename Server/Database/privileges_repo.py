from sqlalchemy.orm import Session
from .models import PrivilegesModel
from Domain.privileges import *
# class PrivilegesRepo:
#     def get_all_privileges(cursor: mysql.connector.connection.MySQLCursor):
#         query = ("SELECT * FROM privileges")
#         cursor.execute(query)
#         results = []
#         for (chatID, username, send, receive, addUser, deleteMessage, deleteChat) in cursor:
#             results.append({"chatID":chatID})
#         return results

# uid | accountUID | send | receive | addUser | deleteMessage | deleteChat

def get_all_privileges(db: Session, limit: int = 100):
    return db.query(PrivilegesModel).limit(limit).all()

def get_privileges(db: Session, id: int):
    return db.query(PrivilegesModel).filter(PrivilegesModel.id == id).first()

def create_privileges(db: Session, privilege: PrivilegesCreate, chat_id: int) -> PrivilegesModel:
    db_privileges = PrivilegesModel(**privilege.dict(), chat_id=chat_id)
    db.add(db_privileges)
    db.commit()
    db.refresh(db_privileges)
    return db_privileges

def update_privileges(db: Session, id: int, privilege: Privileges):
    db_privileges = db.query(PrivilegesModel).filter(PrivilegesModel.id == id)
    if db_privileges is None:
        return
    else:
        db_privileges.update(privilege.dict())
        return db_privileges
    
def delete_privileges(db: Session, id: int) -> bool:
    db_privileges = db.query(PrivilegesModel).filter(PrivilegesModel.id == id)
    if db_privileges is None:
        return False
    else:
        db_privileges.delete()
        db.commit()
        return True