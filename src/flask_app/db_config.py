'''Database configuration'''

from typing import Dict, Any

class FlaskDatabaseConfig:
  '''Database configuration'''

  def __init__(self,
               POSTGRES_HOST: str,
               POSTGRES_USER: str,
               POSTGRES_PASSWORD: str,
               POSTGRES_DB: str) -> None:
    """Configuration object for the database."""
    self.SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                                   f"@{POSTGRES_HOST}:5432/{POSTGRES_DB}"

    engine_options: Dict[str, Any] = {
      'pool_pre_ping': True
    }

    self.SQLALCHEMY_ENGINE_OPTIONS = engine_options
    self.SQLALCHEMY_TRACK_MODIFICATIONS = False