#!/usr/bin/python3
""" a python file that contains the class definition of a State"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

    def __str__(self):
        return f'{self.id}: {self.name}'


if __name__ == "__main__":
    engine = create_engine('\
mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                           sys.argv[2],
                                           sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(engine)()
    statesList = session.query(State).filter(State.name.like('%a%')).all()
    if len(statesList) != 0:
        for state in statesList:
            print(state)
    else:
        print("Nothing")
