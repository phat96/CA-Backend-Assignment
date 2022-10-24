"""This module provides means to perform operations on the database
using the SQLAlchemy library."""

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def init(app: Flask) -> None:
    db.init_app(app)
    from app import models
    migrate.init_app(app, db)

