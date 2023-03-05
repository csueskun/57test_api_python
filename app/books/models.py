from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from ..connection import Base

# define the book model
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    isbn = Column(String)
    year = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
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

    def __repr__(self) -> str:
        return f"<Page(number={self.number}, book='{self.book.title}')>"

    # define a method that returns the page data as a dictionary
    def as_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
