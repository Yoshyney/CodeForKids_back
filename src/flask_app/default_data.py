from logging import Logger

from src.flask_app.db_extensions import db
from src.flask_app.models import Exercice, Tags, TagsByExercice


def init_default_data(log: Logger):

    ## Add 2 exercices !

    exercice1 = Exercice(
        name="Exercice 1 : Avancer le cube. Phase 1 !",
        description="Dans cet exercice, vous allez devoir avancer le cube avec la commande Move jusqu'a la fin !",
        level=
        {
            "start": {"x": -75, "y": 25, "z": 25},
            "end": {"x": 75, "y": 25, "z": 25},
            "level":
                [
                    {"x": -75, "y": 25, "z": 25},
                    {"x": -25, "y": 25, "z": 25},
                    {"x": 25, "y": 25, "z": 25},
                    {"x": 75, "y": 25, "z": 25}
                ]
        }
    )

    exercice2 = Exercice(
        name="Exercice 2 : Avancer le cube. Phase 2 !",
        description="Dans cet exercice, vous allez devoir avancer le cube avec la commande Move ainsi que la "
                    "commande while jusqu'a la fin !",
        level=
        {
            "start": {"x": -75, "y": 25, "z": 25},
            "end": {"x": 75, "y": 25, "z": 25},
            "level":
                [
                    {"x": -75, "y": 25, "z": 25},
                    {"x": -25, "y": 25, "z": 25},
                    {"x": 25, "y": 25, "z": 25},
                    {"x": 75, "y": 25, "z": 25}
                ]
        }
    )

    db.session.add_all([exercice1, exercice2])

    ## Add 2 tags !

    tag1 = Tags(
        name="MOVE LEFT",
        value="move_left"
    )

    tag2 = Tags(
        name="WHILE",
        value="while"
    )

    db.session.add_all([tag1, tag2])
    db.session.commit()

    TagByExo1 = TagsByExercice(
        tag_id=tag1.id,
        exercice_id=exercice1.id
    )

    TagByExo2 = TagsByExercice(
        tag_id=tag1.id,
        exercice_id=exercice2.id
    )

    TagByExo3 = TagsByExercice(
        tag_id=tag2.id,
        exercice_id=exercice2.id
    )

    db.session.add_all([TagByExo1, TagByExo2, TagByExo3])
    db.session.commit()

    log.info("Bdd has been populated with success !")