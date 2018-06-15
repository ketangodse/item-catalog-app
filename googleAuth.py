'use strict'
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable = False)
    name = Column(String(100), nullable=True)
    avatar = Column(String(200))
    active = Column(Boolean, default=False)
    tokens = Column(Text)
    created_at = Column(DateTime, nullable=True)

engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.create_all(engine)