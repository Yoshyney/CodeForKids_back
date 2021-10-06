
import sqlalchemy

from src.config_loader import ConfigLoader
from src.flask_app.db_config import FlaskDatabaseConfig
from flask import Flask
from logbook import Logger
from flask_sqlalchemy import SQLAlchemy # type: ignore

class Flask_app:

    def __init__(self,
                 log: Logger,
                 config: ConfigLoader):
        self.__log = log
        self.__config = config
        self.__schema = "code_for_kids"
        self.__meta = None
        self.__db = None
        self.__flask_app = None

    def __init_flask_app(self) -> None:
        self.__log.info("Init the creation of the Flask application.")
        self.__create_app()
        self.__log.info("Flask Application Created.")

    def __create_app(self) -> None:
        '''Create flask application'''
        self.__flask_app = Flask(__name__)
        db_config = FlaskDatabaseConfig(**self.__config.get_config_file_values("db"))
        self.__flask_app.config.from_object(db_config)
        self.__register_flask_extensions()

    def __register_flask_extensions(self) -> None:
        '''create and registerflask application extensions'''
        self.__meta = sqlalchemy.MetaData(schema=self.__schema)
        self.__db = SQLAlchemy(metadata=self.__meta)
        self.__db.init_app(self.__flask_app)
        self.__log.info("Flask extensions registered.")

    def __regenerate_db(self) -> None:
        self.__db.session.execute(f"CREATE SCHEMA IF NOT EXISTS {self.__schema}")
        self.__db.session.commit()
        # if dev
        self.__db.drop_all()
        self.__db.create_all()
        self.__db.session.commit()


    def setup(self) -> None:
        self.__init_flask_app()
        ## init channel / route ....
        with self.__flask_app.app_context():
            self.__regenerate_db()