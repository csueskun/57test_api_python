from pyparsing import traceback
from .models import Book
from ..connection import database_session
from ..server.security import check_token

class BookHandler:

    # Retrieves all books from the database and returns them as a list of dictionaries.
    def get_all_books(request, _={}):
        try:
            with database_session() as session:
                # Query the database for all Book objects and convert each object to a dictionary.
                books = session.query(Book).filter_by(public=True).all()   
                book_list = [book.as_dict() for book in books]
            return (200, book_list, 'json')
        except:
            # If an error occurs, return a 500 status code.
            print(traceback.format_exc())
            return (500, )

    # Retrieves all books from the database and returns them as a list of dictionaries.
    @check_token
    def get_my_books(request, params={}):
        try:
            with database_session() as session:
                # Query the database for all Book objects and convert each object to a dictionary.
                books = session.query(Book).filter_by(
                    user_id=params.get('user_id')).all()
                book_list = [book.as_dict() for book in books]
            return (200, book_list, 'json')
        except:
            # If an error occurs, return a 500 status code.
            return (500, )

    # Retrieves a specific book by ID and returns it as a dictionary.
    def get_book_by_id(request, params={}):
        # Get the book ID from the request parameters.
        book_id = params.get('book_id', None)
        if not book_id:
            # If no book ID was provided, return a 400 status code.
            return (400, )
        try:
            with database_session() as session:
                # Query the database for the Book object by id.
                book = session.query(Book).filter_by(id=book_id).first()
                if book:
                    # If a Book object is found, returns it as a dictionary.
                    return (200, book.as_dict(), 'json')
            # If no Book object was found, return a 404 status code.
            return (404, )
        except:
            # If an error occurs, return a 500 status code.
            return (500, )

    
    # create a new book
    @check_token
    def register_book(request, params={}):
        # get request data
        data = request.get_post_data()
        try:
            with database_session() as session:
                # Create a new book object and set its attributes
                book = Book(
                    title=data.get('title', ''),
                    author=data.get('author', ''),
                    isbn=data.get('isbn', ''),
                    year=data.get('year', ''),
                    user_id=params.get('user_id'),
                    public=int(data.get('public', '0')),
                )
                # Add the book to the session
                session.add(book)
                # Save the book to the database to get its ID
                session.flush()
                # Commit the session to the database to save all changes
                session.commit()
                return (200, 'Book created')
            return (404, )
        except:
            # If an error occurs, return a 500 status code.
            return (500, )

    # update book
    @check_token
    def update_book(request, params={}):
        # Validate email
        data = request.get_post_data()
        try:
            with database_session() as session:
                # Query the database for the Book object by id
                book = session.query(Book).filter_by(
                    id=params.get('book_id')).first()
                # validate book for author
                if params.get('user_id') != book.user_id:
                    return (403, 'You can\'t update other peoples\'s books') 
                # update books fields with request data
                if 'title' in data:
                    book.title=data.get('title', '')
                if 'author' in data:
                    book.author=data.get('author', '')
                if 'isbn' in data:
                    book.isbn=data.get('isbn', '')
                if 'year' in data:
                    book.year=data.get('year', '')
                if 'public' in data:
                    book.public=int(data.get('public', '0'))
                # Save the book to the database
                session.flush()
                # Commit the session to the database to save all changes
                session.commit()
                return (200, book.as_dict())
            return (404, )
        except:
            # If an error occurs, return a 500 status code.
            return (500, )

