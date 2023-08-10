from typing import List
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = Table(
    "association_table",
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('groupId', Integer, ForeignKey('groups.id')),
    Column('userlId', String, ForeignKey('users.id'))
)

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    users = relationship("User", backref="Group", secondary=association_table)


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    groups = relationship("Group", backref="User", secondary=association_table)
    

# class ProjectUser(Base):
#     __tablename__ = "project_users"

#     id = Column(Integer, primary_key=True)
#     notes = Column(String, nullable=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     project_id = Column(Integer, ForeignKey('projects.id'))