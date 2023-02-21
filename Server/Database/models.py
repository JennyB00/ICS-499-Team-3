from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, LargeBinary
from sqlalchemy.orm import relationship

from .Database import Base

class AccountModel(Base):
    __tablename__ = "accounts"
    username = Column(String(255), primary_key=True, index=True)
    password = Column(String(255))

    contacts = relationship("ContactModel", back_populates="owner")

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

    privileges = relationship("PrivilegesModel", back_populates="chat")
    messages = relationship("MessageModel", back_populates="owner_chat")

class PrivilegesModel(Base):
    __tablename__ = "privileges"
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    username = Column(String(255), ForeignKey("accounts.username"))
    send = Column(Boolean, index=True)
    receive = Column(Boolean, index=True)
    addUser = Column(Boolean)
    deleteMessege = Column(Boolean)
    deleteChat = Column(Boolean)

    owner_chat = relationship("ChatModel", back_populates="privileges")

class MessageModel(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    username = Column(String(255), ForeignKey("accounts.username"))
    date = Column(DateTime)
    type = Column(String(255), index=True)
    message = Column(LargeBinary(500), index=True)

    owner_chat = relationship("ChatModel", back_populates="messages")