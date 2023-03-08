from pyparsing import traceback
from .models import User, Session
from ..connection import database_session
import re, datetime

class UserHandler:

    # create a new user
    def register_user(request, params={}):
        # Validate email
        data = request.get_post_data()
        email = data.get('email', '')
        valid_email, msg = email_is_valid(email)
        if not valid_email:
            return (400, msg)
        # Validate password
        password = data.get('password', '')
        valid_password, msg = password_is_valid(password)
        if not valid_password:
            return (400, msg)
        try:
            with database_session() as session:
                # Create a new user object and set its attributes
                user = User(email=email, password=password)
                # Add the user to the session
                session.add(user)
                # Save the user to the database to get its ID
                session.flush()
                # Commit the session to the database to save all changes
                session.commit()
                return (200, 'User created')
            return (404, )
        except:
            # If an error occurs, return a 500 status code.
            return (500, )

    # create a new user
    def login(request, params={}):
        # Validate email
        data = request.get_post_data()
        email = data.get('email', '')
        valid_email, msg = email_is_valid(email, True)
        if not valid_email:
            return (400, msg)
        # Validate password
        password = data.get('password', '')
        valid_password, msg = password_is_valid(password)
        if not valid_password:
            return (400, msg)
        try:
            with database_session() as session:
                # query database for an user with given data
                user = session.query(User).filter_by(
                    email=email, password=password).first()
                if not user:
                    return (401, 'You have entered an invalid ' \
                        'email or password')

                session_ = Session(user=user, token=new_token())
                session.add(session_)
                # Save the user to the database to get its ID
                session.flush()
                # Commit the session to the database to save all changes
                session.commit()
                return (200, {'token': session_.token})
        except:
            print(traceback.format_exc())
            # If an error occurs, return a 500 status code.
            return (500, )

def email_is_valid(email, login=False):
    # Call pattern validation
    valid, msg = email_pattern_validation(email)
    # if not valid return message
    if not valid:
        return False, msg
    # Call existing validation
    valid, msg = email_exists_validation(email)
    # if not valid return message
    if login:
        if valid:
            return False, 'Email not found.'
    else:
        if not valid:
            return False, msg
    return True, ''

def email_pattern_validation(email):
    # init correct pattern for emails
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    # try to match
    if not re.match(pattern, email):
        # return false and message when not match
        return False, '"{}" has not a valid email format'.format(email)
    # return when match found
    return True, ''

def email_exists_validation(email):
    # init databa session context
    with database_session() as session:
        # search by email
        user = session.query(User).filter_by(email=email).first()
        if user:
            # return false and message when found
            return False, 'Email "{}" already exists'.format(email)
        # return when email is not used yet
        return True, ''

def password_is_valid(password):
    # calculating the length
    if len(password) < 10:
        return False, 'Password needs to contain at least 10 characters'
    # searching for uppercase
    if re.search(r"[A-Z]", password) is None:
        return False, 'Password needs to contain at least 1 uppercase letter'
    # searching for lowercase
    if re.search(r"[a-z]", password) is None:
        return False, 'Password needs to contain at least 1 lowercase letter'
    # searching for symbols
    if re.search(r"[ !@#\]"+r'"]', password) is None:
        return False, 'Password needs to contain at least 1 ' \
            'of the following characters: !, @, #, ?, ]'
    return True, ''    

def new_token():
    token = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    token = hash(token)
    token = abs(int(token))
    return token
