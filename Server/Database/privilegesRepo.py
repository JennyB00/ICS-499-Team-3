from sqlalchemy.orm import Session
from models import PrivilegesModel
from Domain.privileges import Privileges
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

def add_privileges(db: Session, privilege: Privileges, chat_id: int):

    db_privileges = PrivilegesModel(**privilege.dict(), chat_id=chat_id)
    db.add(db_privileges)
    db.commit()
    db.refresh(db_privileges)
    return db_privileges