from app.books.models import Book, User
from app.connection import Session
import random

# Get a session object to work with the database
session = Session()

def seed():
    # A tuple of book data to be added to the database
    users_data = (
        ('csueskun@gmail.com', '@1234567Ab'),
        ('user@57blocks.com', '#1234567Cd'),
    )
    users = []
    for user_ in users_data:
        user = User(email=user_[0], password=user_[1])
        users.append(user)

    # A tuple of book data to be added to the database
    book_data = (
        ('Don Quixote', 'Miguel de Cervantes', '978-0060934347', 1605),
        ('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', '978-0060883287', 1967),
        ('The Odyssey', 'Homer', '978-0140268867', 1488),
        ('The Brothers Karamazov', 'Fyodor Dostoevsky', '978-0374528379', 1880),
        ('The Adventures of Huckleberry Finn', 'Mark Twain', '978-0486280615', 1885),
    )

    # Add each book to the database and its pages
    for book_ in book_data:
        # Create a new book object and set its attributes
        book = Book(
            title=book_[0],
            author=book_[1],
            isbn=book_[2],
            year=book_[3],
            user=random.choice(users),
            public=random.choice((True, False))
        )

        # Add the book to the session
        session.add(book)

        # Save the book to the database to get its ID
        session.flush()

    # Commit the session to the database to save all changes
    session.commit()

if __name__ == '__main__':
    # Call the seed function to populate the database
    seed()
