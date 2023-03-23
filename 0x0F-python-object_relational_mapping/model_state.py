#!/usr/bin/python3
"""contains the class definition of a State
and an instance Base = declarative_base()
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Sequence, String

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, Sequence('states_id_seq'), primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)

