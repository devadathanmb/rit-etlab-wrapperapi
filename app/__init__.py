from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    from app.routes import status, login, profile, logout, attendance, timetable

    app.register_blueprint(status.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(profile.bp)
    app.register_blueprint(logout.bp)
    app.register_blueprint(attendance.bp)
    app.register_blueprint(timetable.bp)

    return app
