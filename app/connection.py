from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# create the SQLAlchemy engine
engine = create_engine('sqlite:///data/books.db')

# create a scoped session factory that uses the engine to create sessions
Session = scoped_session(sessionmaker(bind=engine))

# create a base class for declarative models to inherit from
Base = declarative_base()

@contextmanager
def database_session():
    # create a new session from the session factory
    session = Session()
    try:
        # yield the session to the caller
        yield session
    except:
        # if an exception is raised, rollback the session
        session.rollback()
        # re-raise the exception so it can be handled by the caller
        raise
    finally:
        # close the session when the context manager exits
        session.close()
