from sqlalchemy import ForeignKey

from app import db
from flask_imp.utilities import class_field


def example_function():
    print("example_function printed this message")


class ExampleTable(db.Model):
    example_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(class_field("ExampleUser", "user_id")))
    thing = db.Column(db.String(256), nullable=False)

    @classmethod
    def get_first(cls):
        return cls.query.first()

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()


class ExampleTableOne(db.Model):
    example_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(class_field("ExampleUser", "user_id")))
    thing = db.Column(db.String(256), nullable=False)
