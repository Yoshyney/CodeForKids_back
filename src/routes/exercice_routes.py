
from flask import Blueprint, jsonify

from src.controller.exercice import ExerciceController


def routes(
        exercice: ExerciceController
):

    bp = Blueprint('Exercice', __name__)

    @bp.route('/exercice/<exercice_id>', methods=['GET'])
    def get_exercice(exercice_id: int):
        return jsonify(exercice.handle_event(
            type="get_exercice",
            event={
                "id": exercice_id
            }
        ))

    return bp