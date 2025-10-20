from flask import Flask

app = Flask(__name__)

from app.user import user_routes
from app.category import category_routes
from app.record import record_routes
from app.views import views_routes