MOVIES = [
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
        "description": "A former marine becomes involved in the conflict on Pandora."
    },
    {
        "title": "Gladiator",
        "release_year": 2000,
        "rating": 8.5,
        "description": "A Roman general seeks revenge after being betrayed."
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
        "description": "The aging head of a crime family transfers control to his reluctant son."
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


MOVIE_DETAILS = {

    "Inception": {
        "actors": [
            {"name": "Leonardo DiCaprio"},
            {"name": "Joseph Gordon-Levitt"},
            {"name": "Tom Hardy"}
        ],
        "directors": [
            {"name": "Christopher Nolan"}
        ],
        "genres": [
            {"name": "Sci-Fi"},
            {"name": "Thriller"}
        ]
    },

    "Interstellar": {
        "actors": [
            {"name": "Matthew McConaughey"},
            {"name": "Anne Hathaway"},
            {"name": "Jessica Chastain"}
        ],
        "directors": [
            {"name": "Christopher Nolan"}
        ],
        "genres": [
            {"name": "Sci-Fi"},
            {"name": "Drama"}
        ]
    },

    "The Dark Knight": {
        "actors": [
            {"name": "Christian Bale"},
            {"name": "Heath Ledger"},
            {"name": "Gary Oldman"}
        ],
        "directors": [
            {"name": "Christopher Nolan"}
        ],
        "genres": [
            {"name": "Action"},
            {"name": "Crime"}
        ]
    },

    "The Prestige": {
        "actors": [
            {"name": "Christian Bale"},
            {"name": "Hugh Jackman"},
            {"name": "Scarlett Johansson"}
        ],
        "directors": [
            {"name": "Christopher Nolan"}
        ],
        "genres": [
            {"name": "Drama"},
            {"name": "Mystery"}
        ]
    },

    "The Matrix": {
        "actors": [
            {"name": "Keanu Reeves"},
            {"name": "Laurence Fishburne"},
            {"name": "Hugo Weaving"}
        ],
        "directors": [
            {"name": "Lana Wachowski"}
        ],
        "genres": [
            {"name": "Sci-Fi"},
            {"name": "Action"}
        ]
    },

    "The Revenant": {
        "actors": [
            {"name": "Leonardo DiCaprio"},
            {"name": "Tom Hardy"}
        ],
        "directors": [
            {"name": "Alejandro G. Iñárritu"}
        ],
        "genres": [
            {"name": "Adventure"},
            {"name": "Drama"}
        ]
    },

    "The Departed": {
        "actors": [
            {"name": "Leonardo DiCaprio"},
            {"name": "Matt Damon"},
            {"name": "Mark Wahlberg"}
        ],
        "directors": [
            {"name": "Martin Scorsese"}
        ],
        "genres": [
            {"name": "Crime"},
            {"name": "Thriller"}
        ]
    }
}


ACTOR_RECOMMENDATIONS = {

    "Inception": [
        {
            "movie": {
                "title": "The Revenant",
                "release_year": 2015,
                "rating": 8.0
            },
            "shared_actors": 2
        },
        {
            "movie": {
                "title": "The Departed",
                "release_year": 2006,
                "rating": 8.5
            },
            "shared_actors": 1
        }
    ]
}


GENRE_RECOMMENDATIONS = {

    "Inception": [
        {
            "movie": {
                "title": "Interstellar",
                "release_year": 2014,
                "rating": 8.7
            },
            "shared_genres": 1
        },
        {
            "movie": {
                "title": "The Matrix",
                "release_year": 1999,
                "rating": 8.7
            },
            "shared_genres": 1
        }
    ]
}