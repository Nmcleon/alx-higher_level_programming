#!/usr/bin/python3
"""Defines State class"""

import sys
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

# Declarative base instance
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

# class State definition
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
