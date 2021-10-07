from typing import Any, Dict

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
            "get_exercice": self.__get_exercice
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