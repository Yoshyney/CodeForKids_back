from typing import Any, Dict, Tuple, List

from logbook import Logger

from src.flask_app.db_extensions import db
from src.flask_app.models import Exercice, Tags, TagsByExercice


class ExerciceController:

    def __init__(self,
                 log: Logger,
                 ) -> None:
        self.__log = log

    def handle_event(self,
                     type: str,
                     event: Any) -> Any:
        '''Event handler coming from routes'''

        mapper = {
            "get_exercice": self.__get_exercice,
            "test_exercice": self.__test_exercice
        }

        func = mapper.get(type, None)
        assert func, 'Method {} not allowed'.format(type)
        return func(**event)


    def __get_exercice(self,
                       id: int) -> Dict[str, Any]:
        self.__log.info(f"get_exercice with id : {id}")
        exercice = db.session.query(Exercice).get(id)
        assert exercice
        return exercice.to_dict()

    def __test_exercice(self,
                           id: int,
                           commands: Dict[str, Any]) -> Dict[str, Any]:
        self.__log.info(f"compile_exercice with id : {id}, command: {commands}")
        exercice = db.session.query(Exercice).get(id)
        assert exercice
        positions, succeeded = self.__compile_with_tags(exercice.level, commands)
        return {
            "positions": positions,
            "succeeded": succeeded
        }

    def __compile_with_tags(self,
                            level: Dict[str, Any],
                            commands: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], bool]:
        Actual_position = level['start']
        positions = [Actual_position.copy()]
        for x in range(0, len(commands)):
            if commands[x]['value'] == "move_left":
                Actual_position['x'] += 50
                positions.append(Actual_position.copy())
            if commands[x]['value'] == "while":
                bite = x
                y = x
                while y != len(commands):
                    if commands[y]['value'] == "move_left":
                        Actual_position['x'] += 50
                        positions.append(Actual_position.copy())
                    if self.__verify_values(Actual_position, level['end']) == 3:
                        return (positions, True)
                    if y == len(commands) - 1:
                        y = bite
                    else:
                        y += 1
            if self.__verify_values(Actual_position, level['end']) == 3:
                return (positions, True)
        return (positions, False)

    def __verify_values(self,
                        actual_value: Dict[str, Any],
                        end_value: Dict[str, Any]) -> int:
        return len([k for k in actual_value if k in end_value and actual_value[k] == end_value[k]])

