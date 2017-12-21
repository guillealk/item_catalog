import os
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


class Catalog(Base):
    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, cascade="save-update")

    items = relationship("CatalogItem", back_populates="catalog")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'user_id':self.user_id
        }


class CatalogItem(Base):
    __tablename__ = 'catalog_item'

    id = Column(Integer, primary_key=True)
    tittle = Column(String(80), nullable=False)
    description = Column(String(250))
    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    catalog = relationship(Catalog, back_populates="items")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, cascade="save-update")


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'tittle': self.tittle,
            'description': self.description,
            'id': self.id
        }


engine = create_engine('sqlite:///catalog.db')


Base.metadata.create_all(engine)
