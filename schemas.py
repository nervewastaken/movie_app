from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models import Movie, Actor, db  # Import db for the session
from marshmallow import fields

class MovieSchema(SQLAlchemySchema):
    class Meta:
        model = Movie
        load_instance = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    name = auto_field(required=True)
    release_date = auto_field(required=True)
    profit = auto_field()

class ActorSchema(SQLAlchemySchema):
    class Meta:
        model = Actor
        load_instance = True
        sqla_session = db.session

    id = auto_field(dump_only=True)
    name = auto_field(required=True)
    birth_date = auto_field()
    movies_played = fields.Method("get_movies_played", dump_only=True)

    def get_movies_played(self, actor):
        """Fetch a list of movies the actor has played in."""
        return [movie.name for movie in actor.movies]