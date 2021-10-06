from logbook import StreamHandler
import sys


class AppLogger:

    def __init__(self) -> None:
        StreamHandler(sys.stdout).push_application()