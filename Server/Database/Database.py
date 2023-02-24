from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

#Make sure local machine has this actually initialized
url = URL.create(
    "mysql",
    username="root",
    password="ics499Team3",  # plain (unescaped) text
    host="127.0.0.1",
    database="webserver",
)
engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#This will probably need to be moved to the main method
# connection = mysql.connector.connect(user = 'root', password = 'password', host = '127.0.0.1', database = 'webserver')
# cursor = connection.cursor()

# cursor.execute("CREATE TABLE account (username VARCHAR(255), password VARCHAR(255))")
# cursor.execute("CREATE TABLE privileges (chatID INT, username VARCHAR(255), send BOOLEAN, receive BOOLEAN, addUser BOOLEAN, deleteMessage BOOLEAN, deleteChat BOOLEAN)")
# cursor.execute("CREATE TABLE contacts (username VARCHAR(255), contact VARCHAR(255))")
# cursor.execute("CREATE TABLE chat (chatID INT, creator VARCHAR(255))")
# cursor.execute("CREATE TABLE history (chatID INT, username VARCHAR(255), messageDate DATE, messageString TEXT, messageFile BLOB)")

# cursor.close
# connection.close
