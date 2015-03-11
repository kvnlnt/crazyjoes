from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template
from marshmallow import fields
from marshmallow import Schema

app = Flask(__name__)
db = SQLAlchemy(app)

# Models


class Actor(db.Model):
    __tablename__ = 'actor'
    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))


class Film(db.Model):
    __tablename__ = 'film'
    film_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    rating = db.Column(db.String(100))
    release_year = db.Column(db.String(100))


class FilmActor(db.Model):
    __tablename__ = 'film_actor'
    actor_id = db.Column(
        db.Integer, db.ForeignKey('actor.actor_id'), primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.film_id'))


# Schemas

class FilmSchema(Schema):
    film_id = fields.Integer()
    title = fields.String()
    rating = fields.String()
    release_year = fields.String()


class FilmActorSchema(Schema):
    actor_id = fields.Integer()
    film_id = fields.Integer()


film_actor_schema_list = FilmActorSchema(many=True)
film_schema_list = FilmSchema(many=True)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root@localhost/movie_store'


@app.route("/")
def all_films():

    films = Film.query.all()
    result, errors = film_schema_list.dump(films)
    return render_template("all_films.html", films=result)

if __name__ == "__main__":
    app.run()
