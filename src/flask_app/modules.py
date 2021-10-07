from flask import Flask
from logbook import Logger

# Controller
from src.controller.exercice import ExerciceController

# Routes
from src.routes import exercice_routes

class Modules:

    def __init__(self,
                 log: Logger,
                 flask_app: Flask) -> None:
        self.__log = log
        self.__flask_app = flask_app
        self.__modules = {
            "exercice": self.__init_exercice
        }

    def init_and_load_modules(self):
        for keys in self.__modules:
            self.__modules[keys]()
            self.__log.info(f"Module {keys} has been loaded")

    def __init_exercice(self):
        exercice = ExerciceController(Logger("Exercice"))
        self.__flask_app.register_blueprint(exercice_routes.routes(exercice))
