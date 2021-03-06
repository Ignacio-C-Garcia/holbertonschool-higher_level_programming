#!/usr/bin/python3
""" a python file that contains the class definition of a State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """create a table states"""
    __tablename__ = 'states'
    id = Column(Integer,
                nullable=False,
                autoincrement=True,
                unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
