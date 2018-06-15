import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
   

class Catalogs(Base):
    __tablename__ = 'catalog'
    name = Column(String(80), nullable= False)
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    
    @property
    def serialize(self):
        return {
            'name': self.name,
            'userid': self.user_id,
            'id': self.id
        }

class CatalogItems(Base):
    __tablename__ = 'catalog_item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    catalog = relationship(Catalogs)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'userid': self.user_id,
            'id': self.id,
            'description': self.description,
            'catalog_id': self.catalog_id
        }

engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.create_all(engine)
