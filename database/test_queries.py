from database.connection import driver


def test_graph():

    query = """
    MATCH (m:Movie {title: "Inception"})
          <-[:ACTED_IN]-(a:Actor)
          -[:ACTED_IN]->(related:Movie)

    WHERE related <> m

    RETURN
        a.name AS actor,
        related.title AS movie
    """

    with driver.session() as session:

        result = session.run(query)

        for record in result:

            print(
                record["actor"],
                "->",
                record["movie"]
            )


if __name__ == "__main__":
    test_graph()
    driver.close()

SMART_RECOMMENDATIONS = """
MATCH (m:Movie {title: $title})

MATCH (related:Movie)

WHERE related <> m

OPTIONAL MATCH
    (m)<-[:ACTED_IN]-(actor:Actor)-[:ACTED_IN]->(related)

OPTIONAL MATCH
    (m)-[:HAS_GENRE]->(genre:Genre)<-[:HAS_GENRE]-(related)

WITH
    related,
    count(DISTINCT actor) AS shared_actors,
    count(DISTINCT genre) AS shared_genres

WITH
    related,
    shared_actors,
    shared_genres,
    (shared_actors * 3 + shared_genres * 2) AS score

RETURN
    related,
    shared_actors,
    shared_genres,
    score

ORDER BY score DESC

LIMIT 5
"""