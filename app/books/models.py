from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from ..connection import Base
import datetime

# define the book model
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    isbn = Column(String)
    year = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="books")
    public = Column(Boolean)

    def __repr__(self) -> str:
        return f"<Book(id={self.id}, title={self.title})>"

    # define a method that returns the book data as a dictionary
    def as_dict(self) -> dict:
        book_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return book_dict

# define the page model
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    books = relationship("Book", back_populates="user")
    sessions = relationship("Session", back_populates="user")

    def __repr__(self) -> str:
        return f"<Page(email={self.email})>"

    # define a method that returns the user data as a dictionary
    def as_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# define the session model
class Session(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    token = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="sessions")

    def __repr__(self) -> str:
        return f"<Page(user={self.user_id}, created='{self.created_at}')>"

    # define a method that returns the session data as a dictionary
    def as_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
