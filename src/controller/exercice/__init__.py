from typing import Any

from logbook import Logger


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
        }

        func = mapper.get(type, None)
        assert func, 'Method {} not allowed'.format(type)
        return func(**event)