from flask import Blueprint

# basic_views.haejung
haejung = Blueprint('haejung', __name__, url_prefix='/haejung')


@haejung.route('/about_me')
def about_me():
    return f'저는 {__name__}입니다'

@haejung.route('/hello')
def hello():
    return f'안녕하세요~'

@haejung.route('/bye')
def bye():
    return f'아디오스~잘 가세요~'
    
