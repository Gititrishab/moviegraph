SEARCH_MOVIES = """
MATCH (m:Movie)
WHERE toLower(m.title) CONTAINS toLower($search)
RETURN m
ORDER BY m.rating DESC
"""


MOVIE_DETAILS = """
MATCH (m:Movie {title: $title})

OPTIONAL MATCH (a:Actor)-[:ACTED_IN]->(m)

OPTIONAL MATCH (d:Director)-[:DIRECTED]->(m)

OPTIONAL MATCH (m)-[:HAS_GENRE]->(g:Genre)

RETURN
    m,
    collect(DISTINCT a) AS actors,
    collect(DISTINCT d) AS directors,
    collect(DISTINCT g) AS genres
"""


RECOMMEND_BY_ACTORS = """
MATCH (m:Movie {title: $title})
      <-[:ACTED_IN]-(a:Actor)
      -[:ACTED_IN]->(related:Movie)

WHERE related <> m

RETURN
    related,
    count(DISTINCT a) AS shared_actors

ORDER BY shared_actors DESC
LIMIT 5
"""


RECOMMEND_BY_GENRE = """
MATCH (m:Movie {title: $title})
      -[:HAS_GENRE]->(g:Genre)
      <-[:HAS_GENRE]-(related:Movie)

WHERE related <> m

RETURN
    related,
    count(DISTINCT g) AS shared_genres

ORDER BY shared_genres DESC
LIMIT 5
"""
SMART_RECOMMENDATIONS = """
MATCH (m:Movie {title: $title})

MATCH (related:Movie)

WHERE related <> m

OPTIONAL MATCH (m)<-[:ACTED_IN]-(actor:Actor)-[:ACTED_IN]->(related)

OPTIONAL MATCH (m)-[:HAS_GENRE]->(genre:Genre)<-[:HAS_GENRE]-(related)

WITH related,
     count(DISTINCT actor) AS shared_actors,
     count(DISTINCT genre) AS shared_genres

WITH related,
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
GRAPH_DATA = """
MATCH (m:Movie {title: $title})

OPTIONAL MATCH (a:Actor)-[:ACTED_IN]->(m)
OPTIONAL MATCH (d:Director)-[:DIRECTED]->(m)
OPTIONAL MATCH (m)-[:HAS_GENRE]->(g:Genre)

RETURN
    m,
    collect(DISTINCT a) AS actors,
    collect(DISTINCT d) AS directors,
    collect(DISTINCT g) AS genres
"""