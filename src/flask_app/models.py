from src.flask_app.db_extensions import db

class Exercice(db.Model):

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    description = db.Column(db.String())

class Tags(db.Model):
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())