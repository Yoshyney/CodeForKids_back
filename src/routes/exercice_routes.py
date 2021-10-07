
from flask import Blueprint

from src.controller.exercice import ExerciceController


def routes(
        exercice: ExerciceController
):

    bp = Blueprint('Exercice', __name__)

    @bp.route('/hello', methods=['GET'])
    def hello():
        return "hello world"

    return bp