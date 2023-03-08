
# Setting up and Running

## Overview

This guide outlines the steps required to set up and run a Python REST Library API.

Created using Python version 3.6.9

## Allowed routes

|Method| Routes                   | Params                            | Response                  |
| ---- | -------------            | -------                           |:-------------:            |
| POST | /user/                   | user, password                    | Register a new user       |
| POST | /login/                  | user, password                    | Token with session info   |
| GET  | /books/                  |                                   | All books                 |
| GET  | /books/mine/(token)/     |                                   | All books by current user |
| GET  | /book/(book id)/         |                                   | Book by id                |
| POST | /book/(token)/           | title, author, isbn, year, public | Register a new book       |
| POST | /book/(book id)/(token)/ | title, author, isbn, year, public | Update book               |

## Steps

### 1. Clone the project repository

Clone the project repository to your local machine using your preferred method.

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Apply migrations

```
alembic upgrade head
```

### 4. Run seeder

```
python seeder.py
```

### 5. Start server

```
python main.py
```

### 6. Run tests

With project running on port 8000

```
python -m pytest tests/
```



