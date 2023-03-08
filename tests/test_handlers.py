from app.books.book_handler import BookHandler
from app.books.user_handler import UserHandler
from app.server.request_handler import RequestHandler as base_handler

get_all_books = BookHandler.get_all_books
get_book_by_id = BookHandler.get_book_by_id
login = UserHandler.login

def test_get_all_books():
    code, data, format = get_all_books(base_handler, {})
    assert code == 200
    assert type(data) == list
    assert type(format) == str


def test_get_book_by_id():
    _, data, _ = get_all_books(base_handler, {})
    for i, book in enumerate(data):
        if i > 5:
            return
        params = {'book_id': book.get('id')}
        code, book_data, format = get_book_by_id(base_handler ,params)
        assert code == 200
        assert type(book_data) == dict
        assert type(format) == str
