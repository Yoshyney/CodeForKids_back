import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

meta = sqlalchemy.MetaData(schema='code_for_kids')
db = SQLAlchemy(metadata=meta)