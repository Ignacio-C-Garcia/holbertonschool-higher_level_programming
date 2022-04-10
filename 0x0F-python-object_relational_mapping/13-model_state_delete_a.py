#!/usr/bin/python3
""" a python file that contains the class definition of a State"""
import sys
from sqlalchemy import Column, Integer, String, asc, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('\
mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                           sys.argv[2],
                                           sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(engine)()

    list = session.query(State).filter(State.name.like('%a%')).all()
    for item in list:
        session.delete(item)
    session.commit()
