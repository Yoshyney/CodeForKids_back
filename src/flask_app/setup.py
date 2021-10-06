from datetime import time

import flask
from typing import Any

import sqlalchemy
import psycopg2
import psycopg2.sql
import uuid as uuid

from src.config_loader import ConfigLoader
from src.flask_app.db_config import FlaskDatabaseConfig
from flask import Flask, g, request
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
        '''Init the creation of the flask application'''
        self.__log.info("Init the creation of the Flask application.")
        self.__create_app()
        self.__log.info("Flask Application Created.")
        self.__flask_app_response_provider()

    def __create_app(self) -> None:
        '''Create flask application'''
        self.__flask_app = Flask(__name__)
        db_config = FlaskDatabaseConfig(**self.__config.get_config_file_values("db"))
        self.__flask_app.config.from_object(db_config)
        self.__register_flask_extensions()

    def __register_flask_extensions(self) -> None:
        '''create and register flask application extensions'''
        self.__meta = sqlalchemy.MetaData(schema=self.__schema)
        self.__db = SQLAlchemy(metadata=self.__meta)
        self.__db.init_app(self.__flask_app)
        self.__log.info("Flask extensions registered.")

    def __flask_app_response_provider(self) -> None:
        '''Register before and after request and some errors on db'''
        @self.__flask_app.before_request
        def before_request() -> None:
            """Add request reception time & unique ID to request context"""
            g.start = time()
            g.request_id = uuid.uuid4()

        @self.__flask_app.after_request
        def after_request(response: flask.Response) -> flask.Response:
            """Commit database transactions after each request"""
            try:
                self.__db.session.commit()
            except (sqlalchemy.exc.IntegrityError,
                    sqlalchemy.exc.InvalidRequestError,
                    psycopg2.OperationalError) as e:
                self.__db.session.rollback()
            self.__flask_request_logging(response)
            return response

        @self.__flask_app.errorhandler(sqlalchemy.exc.InvalidRequestError)
        def handle_cannot_connect_until_rollback(error: Any) -> Any:
            return 'Database transaction failed due to invalid transaction. Session has been rolled back', \
                   500

        @self.__flask_app.errorhandler(sqlalchemy.exc.IntegrityError)
        def handle_database_integrity_error(error: Any) -> Any:
            return 'Database transaction failed due to invalid transaction. Session has been rolled back', \
                   500

    def __flask_request_logging(self,
                                response: flask.wrappers.Response) -> None:
        self.__log.info(f"[{g.request_id}] [{request.method}] {request.path} - status:{response.status_code} "
                        f"- params: {dict(request.args)} - json : {request.get_json(silent=True)}")


    def __regenerate_db(self) -> None:
        self.__db.session.execute(f"CREATE SCHEMA IF NOT EXISTS {self.__schema}")
        self.__db.session.commit()
        # if dev
        self.__db.drop_all()
        self.__db.create_all()
        self.__db.session.commit()

    def setup(self) -> Any:
        '''Setup the flask application'''
        self.__init_flask_app()
        ## init channel / route ....
        with self.__flask_app.app_context():
            self.__regenerate_db()
            return self

    def run(self):
        '''Run the flask server'''
        self.__log.info("Flask Application Starting.")
        self.__flask_app.run(debug=True, port=5001,
                      host='0.0.0.0',
                      use_reloader=False,
                      threaded=True)