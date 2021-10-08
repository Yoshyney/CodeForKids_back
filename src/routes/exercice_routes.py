
from flask import Blueprint, jsonify, request

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

    @bp.route('/test_exercice/<exercice_id>', methods=['POST'])
    def test_exercice(exercice_id: int):
        data = request.json
        return jsonify(exercice.handle_event(
            type="test_exercice",
            event={
                "id": exercice_id,
                "commands": data['commands']
            }
        ))

    return bp