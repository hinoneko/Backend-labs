from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)

    from app.models import User, Category, Record

    migrate.init_app(app, db)

    from app.user.user_routes import user_bp
    from app.category.category_routes import category_bp
    from app.record.record_routes import record_bp
    from app.views.views_routes import views_bp

    app.register_blueprint(views_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(record_bp)

    return app