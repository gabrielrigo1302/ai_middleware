from neo4j import GraphDatabase
from settings import settings

# driver = GraphDatabase.driver(  # type: ignore
#     settings.NEO4J_URI, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
# )

driver = GraphDatabase.driver(  # type: ignore
    "neo4j+s://89f945a2.databases.neo4j.io", auth=("neo4j", "GbBvOUS1v9HKuUH8YeGz8VY0JQjxCToKlpqmyFsZYCA")
)