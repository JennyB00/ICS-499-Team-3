from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, LargeBinary
from sqlalchemy.orm import relationship
from .database import Base

class AccountModel(Base):
    __tablename__ = "accounts"
    username = Column(String(255), primary_key=True, index=True)
    password = Column(String(255))
    status = Column(String(8), index=True)
    bot_session_id = Column(String(36), index=True)
    contacts = relationship("ContactModel", back_populates="owner")
    past_chats = relationship("PastChatModel", back_populates="owner")

class PastChatModel(Base):
    __tablename__ = "past_chats_table"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), ForeignKey("accounts.username"))
    past_chat_id = Column(Integer, index=True)
    owner = relationship("AccountModel", back_populates="past_chats")

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

class HistoryModel(Base):
    __tablename__ = "histories"
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    owner_chat = relationship("ChatModel", back_populates="history")
    users = relationship("HistoryUserModel", back_populates="owner")
    messages = relationship("MessageModel", back_populates="history")

class HistoryUserModel(Base):
    __tablename__ = "history_users_table"
    id = Column(Integer, primary_key=True)
    user = Column(String(255))
    history_id = Column(Integer, ForeignKey("histories.id"))
    owner = relationship("HistoryModel", back_populates="users")

class MessageModel(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    username = Column(String(255)) # , ForeignKey("accounts.username"))
    date = Column(DateTime)
    type = Column(String(25), index=True)
    message = Column(LargeBinary(500))
    history_id = Column(Integer, ForeignKey("histories.id"))
    history = relationship("HistoryModel", back_populates="messages")