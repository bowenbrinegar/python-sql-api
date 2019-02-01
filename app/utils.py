def actors_to_dict(selection=None):
    results = []
    for actor in selection:
        actor_dict = actor_to_dict(actor)
        results.append(actor_dict)

    return results

def actor_to_dict(selection=None):
    actor_dict = {}
    actor_dict["id"] = selection.actor_id
    actor_dict["first"] = selection.first_name
    actor_dict["last"] = selection.last_name
    actor_dict["last_update"] = selection.last_update

    return actor_dict

def film_ref_to_dict(selection=None):
    results = []
    for ref in selection:
        film_ref = {}
        film_ref["actor_id"] = ref.actor_id
        film_ref["film_id"] = ref.film_id
        film_ref["last_update"] = ref.last_update
        results.append(film_ref)

    return results

def film_to_dict(selection=None):
    film = {}
    film["id"] = selection.film_id
    film["description"] = selection.description
    film["release_year"] = selection.release_year
    film["language_id"] = selection.language_id
    film["original_language_id"] = selection.original_language_id
    film["rental_duration"] = selection.rental_duration
    film["rental_rate"] = selection.rental_rate
    film["length"] = selection.length
    film["replacement_cost"] = selection.replacement_cost
    film["rating"] = selection.rating
    film["special_features"] = selection.special_features
    film["last_update"] = selection.last_update

    return film