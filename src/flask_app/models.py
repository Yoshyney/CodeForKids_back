import sqlalchemy
from sqlalchemy.orm import backref
from typing import Dict, Any

from src.flask_app.db_extensions import db

class DbModel(db.Model):

    __abstract__ = True

    def to_dict(self) -> Dict[str, Any]:
        d = {}
        inspect = sqlalchemy.inspection.inspect(self.__class__)
        for attr in inspect.attrs:
            key = attr.key
            value = getattr(self, key)
            if isinstance(attr, sqlalchemy.orm.properties.ColumnProperty):
                d[key] = value
            if isinstance(attr, sqlalchemy.orm.properties.RelationshipProperty):
                if isinstance(value, list):
                    d[key] = [val.to_dict() for val in value]
                else:
                    d[key] = value.to_dict()
        return d

class Exercice(DbModel):
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    level = db.Column(db.JSON())
    tags_by_exercice = db.relationship("TagsByExercice", lazy="joined")

class TagsByExercice(DbModel):
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True, unique=True)
    tag_id = db.Column(db.Integer(), db.ForeignKey("tags.id"))
    exercice_id = db.Column(db.Integer(), db.ForeignKey("exercice.id"))
    tags = db.relationship("Tags",  lazy="joined")

class Tags(DbModel):
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String())
    value = db.Column(db.String())