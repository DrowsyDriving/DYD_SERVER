from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class AreaInfo(db.Model):
    __tablename__ = "areainfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.String(255), nullable=False, unique=True)
    areacode = db.Column(db.String(255), nullable=False)


class AlertInfo(db.Model):
    __tablename__ = "alertinfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_number = db.Column(db.String(15), nullable=False)
    warning_level = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Numeric(precision=16, scale=13), nullable=False)
    longitude = db.Column(db.Numeric(precision=16, scale=13), nullable=False)
    occurrence_time = db.Column(db.DateTime, default=datetime.now())


# docker exec -e LC_ALL=C.UTF-8 -it server bash
