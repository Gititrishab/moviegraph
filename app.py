import os

from flask import Flask, jsonify, render_template, request

from database.connection import driver

from database.queries import (
    SEARCH_MOVIES,
    MOVIE_DETAILS,
    RECOMMEND_BY_ACTORS,
    RECOMMEND_BY_GENRE,
    SMART_RECOMMENDATIONS,
    GRAPH_DATA,
)

from database.mock_data import (
    MOVIES,
    MOVIE_DETAILS as MOCK_MOVIE_DETAILS,
    ACTOR_RECOMMENDATIONS,
    GENRE_RECOMMENDATIONS,
)


app = Flask(__name__)

MOCK_MODE = os.getenv(
    "MOCK_MODE",
    "false"
).lower() == "true"


def node_to_dict(node):
    """Convert a Neo4j node into a normal Python dictionary."""
    if node is None:
        return None

    return dict(node)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/movie/<path:title>")
def movie_page(title):
    return render_template("movie.html", title=title)

@app.route("/api/movies")
def get_all_movies():

    if MOCK_MODE:
        return jsonify({
            "success": True,
            "movies": MOVIES
        })

    try:

        query = """
        MATCH (m:Movie)
        RETURN m
        ORDER BY m.rating DESC
        """

        with driver.session() as session:
            result = session.run(query)

            movies = [
                node_to_dict(record["m"])
                for record in result
            ]

        return jsonify({
            "success": True,
            "movies": movies
        })

    except Exception as e:

        print("Database error:", e)

        return jsonify({
            "success": False,
            "error": "Unable to connect to the movie database."
        }), 503
    
@app.route("/api/movies/search")
def search_movies():

    search = request.args.get("q", "").strip()

    if not search:
        return jsonify({
            "success": True,
            "movies": []
        })


    if MOCK_MODE:

        results = [
            movie
            for movie in MOVIES
            if search.lower() in movie["title"].lower()
        ]

        results.sort(
            key=lambda movie: movie["rating"],
            reverse=True
        )

        return jsonify({
            "success": True,
            "movies": results
        })


    try:

        with driver.session() as session:

            result = session.run(
                SEARCH_MOVIES,
                search=search
            )

            movies = [
                node_to_dict(record["m"])
                for record in result
            ]


        return jsonify({
            "success": True,
            "movies": movies
        })


    except Exception as e:

        print("Database error:", e)

        return jsonify({
            "success": False,
            "error": "Unable to connect to the movie database."
        }), 503

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html"
    ), 404

@app.errorhandler(500)
def internal_error(error):

    return jsonify({
        "success": False,
        "error": "An internal server error occurred."
    }), 500

@app.route("/api/movies/<path:title>")
def get_movie(title):

    try:
        with driver.session() as session:
            result = session.run(
                MOVIE_DETAILS,
                title=title
            )

            record = result.single()

            if record is None:
                return jsonify({
                    "success": False,
                    "error": "Movie not found."
                }), 404

            movie = node_to_dict(record["m"])

            actors = [
                node_to_dict(actor)
                for actor in record["actors"]
                if actor is not None
            ]

            directors = [
                node_to_dict(director)
                for director in record["directors"]
                if director is not None
            ]

            genres = [
                node_to_dict(genre)
                for genre in record["genres"]
                if genre is not None
            ]

        return jsonify({
            "success": True,
            "movie": movie,
            "actors": actors,
            "directors": directors,
            "genres": genres
        })

    except Exception as e:
        print("Database error:", e)

        return jsonify({
            "success": False,
            "error": "Unable to connect to the movie database."
        }), 503


@app.route("/api/movies/<path:title>/recommendations")
def get_recommendations(title):

    if MOCK_MODE:

        actor_recommendations = (
            ACTOR_RECOMMENDATIONS.get(title, [])
        )

        genre_recommendations = (
            GENRE_RECOMMENDATIONS.get(title, [])
        )

        return jsonify({
            "success": True,
            "by_actors": actor_recommendations,
            "by_genres": genre_recommendations,
            "smart": []
        })


    try:

        recommendations = []

        with driver.session() as session:

            result = session.run(
                SMART_RECOMMENDATIONS,
                title=title
            )

            for record in result:

                movie = node_to_dict(
                    record["related"]
                )

                recommendations.append({
                    "movie": movie,
                    "shared_actors":
                        record["shared_actors"],
                    "shared_genres":
                        record["shared_genres"],
                    "score":
                        record["score"]
                })


        return jsonify({
            "success": True,
            "recommendations": recommendations
        })


    except Exception as e:

        print("Database error:", e)

        return jsonify({
            "success": False,
            "error": "Unable to generate recommendations."
        }), 503


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "success": False,
        "error": "Page not found."
    }), 404

@app.route("/api/movies/<path:title>/graph")
def get_graph(title):

    if MOCK_MODE:
        return jsonify({
            "success": True,
            "nodes": [],
            "edges": []
        })

    try:

        nodes = []
        edges = []

        with driver.session() as session:

            result = session.run(
                GRAPH_DATA,
                title=title
            )

            record = result.single()

            if record is None:
                return jsonify({
                    "success": False,
                    "error": "Movie not found."
                }), 404

            movie = record["m"]
            actors = record["actors"]
            directors = record["directors"]
            genres = record["genres"]

            movie_id = f"movie-{movie['title']}"

            nodes.append({
                "data": {
                    "id": movie_id,
                    "label": movie["title"],
                    "type": "Movie"
                }
            })

            for actor in actors:

                if actor is None:
                    continue

                actor_id = f"actor-{actor['name']}"

                nodes.append({
                    "data": {
                        "id": actor_id,
                        "label": actor["name"],
                        "type": "Actor"
                    }
                })

                edges.append({
                    "data": {
                        "source": actor_id,
                        "target": movie_id,
                        "label": "ACTED_IN"
                    }
                })

            for director in directors:

                if director is None:
                    continue

                director_id = f"director-{director['name']}"

                nodes.append({
                    "data": {
                        "id": director_id,
                        "label": director["name"],
                        "type": "Director"
                    }
                })

                edges.append({
                    "data": {
                        "source": director_id,
                        "target": movie_id,
                        "label": "DIRECTED"
                    }
                })

            for genre in genres:

                if genre is None:
                    continue

                genre_id = f"genre-{genre['name']}"

                nodes.append({
                    "data": {
                        "id": genre_id,
                        "label": genre["name"],
                        "type": "Genre"
                    }
                })

                edges.append({
                    "data": {
                        "source": movie_id,
                        "target": genre_id,
                        "label": "HAS_GENRE"
                    }
                })

        return jsonify({
            "success": True,
            "nodes": nodes,
            "edges": edges
        })

    except Exception as e:

        print("Graph error:", e)

        return jsonify({
            "success": False,
            "error": "Unable to load graph."
        }), 503

@app.route("/health")
def health():

    if MOCK_MODE:
        return jsonify({
            "status": "ok",
            "database": "mock"
        })

    try:

        with driver.session() as session:

            result = session.run(
                "RETURN 1 AS value"
            )

            record = result.single()

            if record["value"] == 1:

                return jsonify({
                    "status": "ok",
                    "database": "CognoDB"
                })

    except Exception as e:

        print("Health check error:", e)

        return jsonify({
            "status": "error",
            "database": "CognoDB"
        }), 503

if __name__ == "__main__":
    app.run(debug=True)