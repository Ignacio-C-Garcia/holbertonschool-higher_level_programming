#!/usr/bin/python3
""" a python file that contains the class definition of a State"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """create a table states"""
    __tablename__ = 'cities'
    id = Column(Integer,
                nullable=False,
                autoincrement=True,
                unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('sates.states.id'),
                      nullable=False)
