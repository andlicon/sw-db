import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine, UniqueConstraint
from eralchemy2 import render_er
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

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
    created_at = Column('created_at', TIMESTAMP(True), default=text('now()'))
    update_at = Column('updated_at', TIMESTAMP(True))

    # relationship
    favorites = relationship('Favorite', back_populates='users')

    def login(self):
        pass
    
    def addFavoriet(self):
        pass

class Gender(enum.Enum):
    male = 'male'
    woman = 'woman'
    noDefined = 'noDef'

class Species(enum.Enum):
    human = 'human'
    wookie = 'wookie'
    robot = 'robot'

class Character(Base):
    __tablename__ = 'characters'

    # attributes
    id = Column('id', Integer, primary_key=True)
    item_id = Column('item_id', Integer, ForeignKey('items.id'))
    name = Column('name', String(100), nullable=False)
    height = Column('height', Integer, nullable=False)
    mass = Column('mass', Integer, nullable=False)
    hair_color = Column('hair_color', String(30))
    skin_color = Column('skin_color', String(30), nullable=False)
    birth_Year = Column('birth_year', String(30), nullable=False)
    gender = Column('gender', Enum(Gender), default=(Gender.noDefined))
    species = Column('species', Enum(Species), default=(Species.human))
    created_at = Column('created_at', TIMESTAMP(True), default=text('now()'))
    update_at = Column('updated_at', TIMESTAMP(True))
    
    # relationship
    item = relationship('Item', back_populates='characters')

class Planet(Base):
    __tablename__ = 'planets'

    # atributtes
    id = Column('id', Integer, primary_key=True)
    item_id = Column('item_id', ForeignKey('items.id'))
    name = Column('name', String(100), nullable=False)
    rotation_period = Column('rotation_period', Integer, nullable=False)
    diameter = Column('diameter', Integer, nullable=False)
    climate = Column('climate', String(50), nullable=False)
    gravity = Column('gravity', String(50), nullable=False)
    terrain = Column('terrain', String(50), nullable=False)
    superface_water = Column('superface_water', Integer, nullable=False)
    population = Column('population', Integer, nullable=False)
    created_at = Column('created_at', TIMESTAMP(True), default=text('now()'))
    update_at = Column('updated_at', TIMESTAMP(True))

    # relationship
    item = relationship('Item', back_populates='planets')

class Naturaleza(enum.Enum):
    people = 'people'
    planet = 'planet'

class Favorite(Base):
    __tablename__ = 'favorites'

    # attributes
    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', ForeignKey('users.id'), nullable=False)
    naturaleza = Column('naturaleza', Enum(Naturaleza), nullable=False)
    naturaleza_id = Column('naturaleza_id', Integer, ForeignKey('planets.id'), ForeignKey('characters.id'))

#     # relationship
    characters = relationship('Character', back_populates='favorites')
    planets = relationship('Planet', back_populates='favorites')
    user = relationship('User', back_populates='favorites')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')