import requests

def test_get_books():
    response = requests.get("http://localhost:8000/books/")
    assert response.status_code == 200

def test_get_book_by_id():
    response = requests.get("http://localhost:8000/book/1/")
    assert response.status_code in [200, 404]
