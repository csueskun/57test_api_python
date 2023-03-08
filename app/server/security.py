from functools import wraps
from ..connection import database_session
from ..books.models import Session
from datetime import datetime, timedelta, date

def check_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = args[1].get('token')
        if not token:
            return (401, 'Token not supplied')
        with database_session() as session:
            session_ = session.query(Session).filter_by(token=token).first()
            if datetime.now() > (session_.created_at + timedelta(minutes=200)):
                return (401, 'Session expired')
            args[1]['user_id'] = session_.user.id
        return f(*args, **kwargs)
    return wrapper