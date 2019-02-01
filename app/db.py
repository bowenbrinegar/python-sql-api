import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Text, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("mysql://root:root@localhost/sakila")
session = Session(bind=engine)

Base.metadata.create_all(engine)

class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    last_update = Column(TIMESTAMP)

class FilmLookup(Base):
    __tablename__ = 'film_actor'
    actor_id = Column(Integer)
    film_id = Column(Integer, primary_key=True)
    last_update = Column(TIMESTAMP)

class Film(Base):
    __tablename__ = 'film'
    film_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    release_year = Column(Integer)
    language_id = Column(Integer)
    original_language_id = Column(Integer)
    rental_duration = Column(Integer)
    rental_rate = Column(Float)
    length = Column(Integer)
    replacement_cost = Column(Float)
    rating = Column(String)
    special_features = Column(String)
    last_update = Column(TIMESTAMP)