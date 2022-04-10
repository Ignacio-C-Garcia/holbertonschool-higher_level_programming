#!/usr/bin/python3
""" a python file that contains the class definition of a State"""
import sys
from sqlalchemy import Column, Integer, String, asc, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import Base, City


if __name__ == "__main__":
    engine = create_engine('\
mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                           sys.argv[2],
                                           sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(engine)()

    lista = session.query(State, City).join(City, State.id==City.state_id).order_by(asc(City.id)).all()
    for state, city in lista:
        print(f'{state.name}: ({city.id}) {city.name}')
