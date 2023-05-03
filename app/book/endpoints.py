from flask import Blueprint

book = Blueprint('book', __name__, url_prefix='/book')

@book.get('/all')
def get_all_books():
    return [
        {'name':'James Hardley Chase'}
    ]