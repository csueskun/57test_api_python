from ..books.book_handler import BookHandler
from ..books.user_handler import UserHandler

routes = [
    {
        'path': r'^/books/$',
        'methods': ['GET'],
        'handler': BookHandler.get_all_books
    },
    {
        'path': r'^/books/mine/(?P<token>[0-9]+)/$',
        'methods': ['GET'],
        'handler': BookHandler.get_my_books
    },
    {
        'path': r'^/book/(?P<token>[0-9]+)/$',
        'methods': ['OPTIONS', 'POST'],
        'handler': BookHandler.register_book
    },
    {
        'path': r'^/book/(?P<book_id>[0-9]+)/$',
        'methods': ['GET'],
        'handler': BookHandler.get_book_by_id
    },
    {
        'path': r'^/book/(?P<book_id>[0-9]+)/(?P<token>[0-9]+)/$',
        'methods': ['OPTIONS', 'POST'],
        'handler': BookHandler.update_book
    },
    {
        'path': r'^/user/$',
        'methods': ['OPTIONS', 'POST'],
        'handler': UserHandler.register_user
    },
    {
        'path': r'^/login/$',
        'methods': ['OPTIONS', 'POST'],
        'handler': UserHandler.login
    },
]