from flask import Flask, jsonify
from db import session, Actor, FilmLookup, Film
from utils import actors_to_dict, actor_to_dict, film_ref_to_dict, film_to_dict

app = Flask(__name__)

# routes

@app.route("/")
def api_dictionary():
    return (
        f"Routes<br/>"
        f"/api/v1/actors/all<br/>"
        f"/api/v1/actors/count<br/>"
        f"/api/v1/actors/firstname"
        f"/api/v1/actors/firstname/lastname/films"
    )

@app.route("/api/v1/actors/all")
def actors_all():
    selection = session.query(Actor).all()
    res = actors_to_dict(selection)
    return jsonify(res)

@app.route("/api/v1/actors/<count>")
def actors_by_limit(count=None):
    selection = session.query(Actor).limit(count).all()
    res = actors_to_dict(selection)
    return jsonify(res)

@app.route("/api/v1/actors/<firstname>")
def actors_by_first(firstname=None):
    selection = session.query(Actor).filter_by(first_name=firstname)
    res = actors_to_dict(selection)
    return jsonify(res)

@app.route("/api/v1/actors/<lastname>")
def actors_by_last(lastname=None):
    selection = session.query(Actor).filter_by(last_name=lastname)
    res = actors_to_dict(selection)
    return jsonify(res)

@app.route("/api/v1/actors/<firstname>/<lastname>/films")
def films_by_actor(firstname=None, lastname=None):
    actor = session.query(Actor).filter_by(first_name=firstname, last_name=lastname).first()
    actor_match = actor_to_dict(actor)

    print(actor_match["id"])

    film_refs = session.query(FilmLookup).filter_by(actor_id=actor_match["id"]).all()
    film_refs = film_ref_to_dict(film_refs)

    films = []
    for film in film_refs:
        temp = session.query(Film).filter_by(film_id=film["film_id"]).first()
        film_dict = film_to_dict(temp)
        films.append(film_dict)
    
    return jsonify(films)

if __name__ == '__main__':
    app.run(debug=True)
