from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
    messages = relationship("Message", back_populates="owner")

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="messages")

class IOC(Base):
    __tablename__ = 'iocs'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    value = Column(String)
    created_at = Column(DateTime)
