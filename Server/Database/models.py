from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, LargeBinary, Table
from sqlalchemy.orm import relationship, DeclarativeBase

from .Database import Base

past_chats_table = Table(
    "past_chats",
    DeclarativeBase.metadata,
    Column("user", ForeignKey("accounts.username")),
    Column("past_chat_id", ForeignKey("chats.id")),
)

class AccountModel(Base):
    __tablename__ = "accounts"
    username = Column(String(255), primary_key=True, index=True)
    password = Column(String(255))

    contacts = relationship("ContactModel", back_populates="owner")
    past_chats = relationship(secondary=past_chats_table)

class ContactModel(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    owner_id = Column(String(255), ForeignKey("accounts.username"))
    contact = Column(String(255), index=True)

    owner = relationship("AccountModel", back_populates="contacts")

class ChatModel(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    # creator = Column(String, ForeignKey("accounts.username"))
    history = relationship("HistoryModel", back_populates="owner_chat")
    privileges = relationship("PrivilegesModel", back_populates="owner_chat")

class PrivilegesModel(Base):
    __tablename__ = "privileges"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), ForeignKey("accounts.username"))
    send = Column(Boolean, index=True)
    receive = Column(Boolean, index=True)
    add_user = Column(Boolean)
    delete_messege = Column(Boolean)
    delete_chat = Column(Boolean)

    chat_id = Column(Integer, ForeignKey("chats.id"))
    owner_chat = relationship("ChatModel", back_populates="privileges")

history_users_table = Table(
    "history_users",
    DeclarativeBase.metadata,
    Column("history_id", ForeignKey("histories.id")),
    Column("user", ForeignKey("accounts.username")),
)

class HistoryModel(Base):
    __tablename__ = "histories"
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    owner_chat = relationship("ChatModel", back_populates="")

    users = relationship(secondary=history_users_table)

    messages = relationship("MessageModel", back_populates="history")


class MessageModel(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), ForeignKey("accounts.username"))
    date = Column(DateTime)
    type = Column(String(255), index=True)
    message = Column(LargeBinary(500), index=True)

    history_id = Column(Integer, ForeignKey("history.id"))
    history = relationship("ChatModel", back_populates="messages")