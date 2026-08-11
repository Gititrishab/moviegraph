from database.connection import driver


movies = [
    {
        "title": "Inception",
        "release_year": 2010,
        "rating": 8.8,
        "description": "A thief who steals secrets through dreams is given a chance to erase his past."
    },
    {
        "title": "Interstellar",
        "release_year": 2014,
        "rating": 8.7,
        "description": "Explorers travel through a wormhole in space to find a new home for humanity."
    },
    {
        "title": "The Dark Knight",
        "release_year": 2008,
        "rating": 9.0,
        "description": "Batman faces a criminal mastermind who creates chaos across Gotham."
    },
    {
        "title": "The Prestige",
        "release_year": 2006,
        "rating": 8.5,
        "description": "Two rival magicians become obsessed with creating the ultimate illusion."
    },
    {
        "title": "The Matrix",
        "release_year": 1999,
        "rating": 8.7,
        "description": "A hacker discovers that reality is not what it seems."
    },
    {
        "title": "Avatar",
        "release_year": 2009,
        "rating": 7.9,
        "description": "A former marine becomes involved in the conflict between humans and the inhabitants of Pandora."
    },
    {
        "title": "Gladiator",
        "release_year": 2000,
        "rating": 8.5,
        "description": "A Roman general seeks revenge after being betrayed and forced into slavery."
    },
    {
        "title": "The Revenant",
        "release_year": 2015,
        "rating": 8.0,
        "description": "A frontiersman fights for survival and revenge after being left for dead."
    },
    {
        "title": "Titanic",
        "release_year": 1997,
        "rating": 7.9,
        "description": "Two people from different social backgrounds fall in love aboard the Titanic."
    },
    {
        "title": "Forrest Gump",
        "release_year": 1994,
        "rating": 8.8,
        "description": "A kind-hearted man experiences major events in American history."
    },
    {
        "title": "Pulp Fiction",
        "release_year": 1994,
        "rating": 8.9,
        "description": "Several interconnected stories unfold around criminals in Los Angeles."
    },
    {
        "title": "The Shawshank Redemption",
        "release_year": 1994,
        "rating": 9.3,
        "description": "A prisoner builds an unexpected friendship while maintaining hope for freedom."
    },
    {
        "title": "The Godfather",
        "release_year": 1972,
        "rating": 9.2,
        "description": "The aging head of a crime family transfers control of his empire to his reluctant son."
    },
    {
        "title": "Parasite",
        "release_year": 2019,
        "rating": 8.5,
        "description": "A struggling family gradually becomes involved with a wealthy household."
    },
    {
        "title": "The Departed",
        "release_year": 2006,
        "rating": 8.5,
        "description": "An undercover police officer and a criminal informant try to identify each other."
    }
]


actors = [
    ("Leonardo DiCaprio", "Inception"),
    ("Joseph Gordon-Levitt", "Inception"),
    ("Tom Hardy", "Inception"),
    
    ("Matthew McConaughey", "Interstellar"),
    ("Anne Hathaway", "Interstellar"),
    ("Jessica Chastain", "Interstellar"),
    
    ("Christian Bale", "The Dark Knight"),
    ("Heath Ledger", "The Dark Knight"),
    ("Gary Oldman", "The Dark Knight"),
    
    ("Christian Bale", "The Prestige"),
    ("Hugh Jackman", "The Prestige"),
    ("Scarlett Johansson", "The Prestige"),
    
    ("Keanu Reeves", "The Matrix"),
    ("Laurence Fishburne", "The Matrix"),
    ("Hugo Weaving", "The Matrix"),
    
    ("Sam Worthington", "Avatar"),
    ("Zoe Saldana", "Avatar"),
    ("Sigourney Weaver", "Avatar"),
    
    ("Russell Crowe", "Gladiator"),
    ("Joaquin Phoenix", "Gladiator"),
    
    ("Leonardo DiCaprio", "The Revenant"),
    ("Tom Hardy", "The Revenant"),
    
    ("Leonardo DiCaprio", "Titanic"),
    ("Kate Winslet", "Titanic"),
    
    ("Tom Hanks", "Forrest Gump"),
    ("Robin Wright", "Forrest Gump"),
    
    ("John Travolta", "Pulp Fiction"),
    ("Samuel L. Jackson", "Pulp Fiction"),
    
    ("Tim Robbins", "The Shawshank Redemption"),
    ("Morgan Freeman", "The Shawshank Redemption"),
    
    ("Marlon Brando", "The Godfather"),
    ("Al Pacino", "The Godfather"),
    
    ("Song Kang-ho", "Parasite"),
    ("Lee Sun-kyun", "Parasite"),
    
    ("Leonardo DiCaprio", "The Departed"),
    ("Matt Damon", "The Departed"),
    ("Mark Wahlberg", "The Departed")
]


directors = [
    ("Christopher Nolan", "Inception"),
    ("Christopher Nolan", "Interstellar"),
    ("Christopher Nolan", "The Dark Knight"),
    ("Christopher Nolan", "The Prestige"),
    ("Lana Wachowski", "The Matrix"),
    ("James Cameron", "Avatar"),
    ("Ridley Scott", "Gladiator"),
    ("Alejandro G. Iñárritu", "The Revenant"),
    ("James Cameron", "Titanic"),
    ("Robert Zemeckis", "Forrest Gump"),
    ("Quentin Tarantino", "Pulp Fiction"),
    ("Frank Darabont", "The Shawshank Redemption"),
    ("Francis Ford Coppola", "The Godfather"),
    ("Bong Joon Ho", "Parasite"),
    ("Martin Scorsese", "The Departed")
]


genres = [
    ("Inception", "Sci-Fi"),
    ("Inception", "Thriller"),
    
    ("Interstellar", "Sci-Fi"),
    ("Interstellar", "Drama"),
    
    ("The Dark Knight", "Action"),
    ("The Dark Knight", "Crime"),
    
    ("The Prestige", "Drama"),
    ("The Prestige", "Mystery"),
    
    ("The Matrix", "Sci-Fi"),
    ("The Matrix", "Action"),
    
    ("Avatar", "Sci-Fi"),
    ("Avatar", "Adventure"),
    
    ("Gladiator", "Action"),
    ("Gladiator", "Drama"),
    
    ("The Revenant", "Adventure"),
    ("The Revenant", "Drama"),
    
    ("Titanic", "Drama"),
    ("Titanic", "Romance"),
    
    ("Forrest Gump", "Drama"),
    ("Forrest Gump", "Romance"),
    
    ("Pulp Fiction", "Crime"),
    ("Pulp Fiction", "Drama"),
    
    ("The Shawshank Redemption", "Drama"),
    
    ("The Godfather", "Crime"),
    ("The Godfather", "Drama"),
    
    ("Parasite", "Drama"),
    ("Parasite", "Thriller"),
    
    ("The Departed", "Crime"),
    ("The Departed", "Thriller")
]


def clear_database():
    query = """
    MATCH (n)
    DETACH DELETE n
    """

    with driver.session() as session:
        session.run(query)


def create_movies():
    query = """
    CREATE (m:Movie {
        title: $title,
        release_year: $release_year,
        rating: $rating,
        description: $description
    })
    """

    with driver.session() as session:
        for movie in movies:
            session.run(query, **movie)


def create_actors():
    query = """
    MERGE (a:Actor {name: $actor_name})
    WITH a
    MATCH (m:Movie {title: $movie_title})
    MERGE (a)-[:ACTED_IN]->(m)
    """

    with driver.session() as session:
        for actor_name, movie_title in actors:
            session.run(
                query,
                actor_name=actor_name,
                movie_title=movie_title
            )


def create_directors():
    query = """
    MERGE (d:Director {name: $director_name})
    WITH d
    MATCH (m:Movie {title: $movie_title})
    MERGE (d)-[:DIRECTED]->(m)
    """

    with driver.session() as session:
        for director_name, movie_title in directors:
            session.run(
                query,
                director_name=director_name,
                movie_title=movie_title
            )


def create_genres():
    query = """
    MERGE (g:Genre {name: $genre_name})
    WITH g
    MATCH (m:Movie {title: $movie_title})
    MERGE (m)-[:HAS_GENRE]->(g)
    """

    with driver.session() as session:
        for movie_title, genre_name in genres:
            session.run(
                query,
                movie_title=movie_title,
                genre_name=genre_name
            )


def seed_database():
    print("Clearing database...")
    clear_database()

    print("Creating movies...")
    create_movies()

    print("Creating actors...")
    create_actors()

    print("Creating directors...")
    create_directors()

    print("Creating genres...")
    create_genres()

    print("Database seeded successfully!")


if __name__ == "__main__":
    seed_database()
    driver.close()