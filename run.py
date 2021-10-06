"""Run and start the application"""

from src.config_loader import ConfigLoader
from src.flask_app.setup import Flask_app
from src.logging import AppLogger
from logbook import Logger
import os


def main(config_path: str = "/config"):
    AppLogger()
    config = ConfigLoader(log=Logger("Config-Loader"),
                          path=f"{os.path.dirname(os.path.realpath(__file__))}{config_path}")
    flask_app = Flask_app(log=Logger("Setup"),
                          config=config)
    flask_app.setup().run()

if __name__ == '__main__':
    main()