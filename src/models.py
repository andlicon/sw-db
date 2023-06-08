import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine, UniqueConstraint
from eralchemy2 import render_er

Base = declarative_base()

class UserStatus(enum.Enum):
    invalid = 0
    valid = 1
    baned = 2


class User(Base):
    __tablename__ = 'users'

    # attributes
    id = Column('id', Integer, primary_key=True)
    nickname = Column('nickname', String(40), nullable=False, unique=True)
    password = Column('password', String(40), nullable=False)
    email = Column('email', String(100), nullable=False, unique=True)
    status = Column('status', Enum(UserStatus), nullable=False, default=str(UserStatus.invalid))

    # relationship
    favorites = relationship('Favorite', back_populates='users')

    def login(self):
        pass
    
    def addFavoriet(self):
        pass

class Gender(enum.Enum):
    male = 0
    woman = 1
    noDefined = 2

class ItemType(enum.Enum):
    character = 0
    planet = 1

class Item(Base):
    __tablename__ = 'items'

    # attributes
    id = Column('id', Integer, primary_key=True)
    idCharacter = Column('idCharacter', Integer, unique=True)
    idPlanet = Column('idPlanet', Integer, unique=True)

    # relationship
    characters = relationship('Character', back_populates='items')
    planets = relationship('Planet', back_populates='items')

class Character(Base):
    __tablename__ = 'characters'

    # attributes
    id = Column('id', Integer, primary_key=True)
    itemId = Column('itemId', Integer, ForeignKey('items.id'))
    name = Column('name', String(100), nullable=False)
    height = Column('height', Integer, nullable=False)
    mass = Column('mass', Integer, nullable=False)
    hairColor = Column('hairColor', String(30))
    skinColor = Column('skinColor', String(30), nullable=False)
    birthYear = Column('birthYear', String(30), nullable=False)
    gender = Column('gender', Enum(Gender), default=str(Gender.noDefined))
    homeWorld = Column('homeWorld', Integer, nullable=False)    #Esto sera una foreing
    species = Column('species', Integer, nullable=False)        #Esto sera un foreign
    
    # relationship
    item = relationship('Item', back_populates='characters')

class Planet(Base):
    __tablename__ = 'planets'

    # atributtes
    id = Column('id', Integer, primary_key=True)
    itemId = Column('itemId', ForeignKey('items.id'))
    name = Column('name', String(100), nullable=False)
    rotationPeriod = Column('rotationPeriod', Integer, nullable=False)
    diameter = Column('diameter', Integer, nullable=False)
    climate = Column('climate', String(50), nullable=False)
    gravity = Column('gravity', String(50), nullable=False)
    terrain = Column('terrain', String(50), nullable=False)
    superfaceWater = Column('superfaceWater', Integer, nullable=False)
    population = Column('population', Integer, nullable=False)

    # relationship
    item = relationship('Item', back_populates='planets')

class Favorite(Base):
    __tablename__ = 'favorites'

    # attributes
    id = Column('id', Integer, primary_key=True)
    userId = Column('userId', ForeignKey('users.id'), nullable=False)
    itemId = Column('itemId', ForeignKey('items.id'), nullable=False)

    # relationships
    user = relationship('User', back_populates='favorites')
    item = relationship('Item', back_populates='favorites')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
