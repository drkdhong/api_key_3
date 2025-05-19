from flask import Blueprint

main = Blueprint('main', __name__,static_folder='static', template_folder='templates')

from . import views  # views.py import해서 라우팅 등록
