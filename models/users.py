import bcrypt
from typing import List, Optional
from sqlalchemy import UniqueConstraint, Column, Integer, String, Boolean
from models.base import Base


def hash_password(pw):
    return bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())


def check_password(hashed, pw):
    return bcrypt.checkpw(pw.encode('utf8'), hashed.encode('utf8'))


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (UniqueConstraint('email'),)

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    profile_pic = Column(String)
    is_staff = Column(Boolean, default=False)
