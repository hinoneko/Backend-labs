import os
import time

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, init, migrate as fmigrate, upgrade, stamp
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def is_first_run():
    return not os.path.exists('migrations')


def migrate_db(app):
    with app.app_context():
        if is_first_run():
            init()
            stamp()

        fmigrate(message="Auto migration")

        upgrade()


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    jwt.init_app(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            "message": "The token has expired.",
            "error": "token_expired"
        }), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            "message": "Signature verification failed.",
            "error": "invalid_token"
        }), 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            "description": "Request does not contain an access token.",
            "error": "authorization_required"
        }), 401

    from app.models import User, Category, Record

    migrate.init_app(app, db)
    time.sleep(5)
    migrate_db(app)

    from app.user.user_routes import user_bp
    from app.category.category_routes import category_bp
    from app.record.record_routes import record_bp
    from app.views.views_routes import views_bp
    from app.auth.auth_routes import auth_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(views_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(record_bp)

    return app