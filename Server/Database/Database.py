from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, declarative_base

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