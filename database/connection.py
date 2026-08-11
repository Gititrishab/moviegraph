# import os
# from pathlib import Path

# from dotenv import load_dotenv
# from neo4j import GraphDatabase


# # Project root: D:\moviegraph
# BASE_DIR = Path(__file__).resolve().parent.parent

# # .env location: D:\moviegraph\.env
# ENV_FILE = BASE_DIR / ".env"

# print("Looking for .env at:", ENV_FILE)
# print("Does .env exist?:", ENV_FILE.exists())

# load_dotenv(dotenv_path=ENV_FILE)

# URI = os.getenv("bolt+s://db-1798c4ca.databases.cognodb.com")
# USERNAME = os.getenv("cognodb")
# PASSWORD = os.getenv("********")

# print("URI LOADED:", URI is not None)
# print("USERNAME:", USERNAME)
# print("PASSWORD LOADED:", PASSWORD is not None)

# if not URI:
#     raise ValueError("COGNODB_URI is missing from .env")

# if not USERNAME:
#     raise ValueError("COGNODB_USERNAME is missing from .env")

# if not PASSWORD:
#     raise ValueError("COGNODB_PASSWORD is missing from .env")


# driver = GraphDatabase.driver(
#     URI,
#     auth=(USERNAME, PASSWORD)
# )


# def close_driver():
#     driver.close()

import os
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")
MOCK_MODE = os.getenv("MOCK_MODE", "false").lower() == "true"


driver = None

if not MOCK_MODE:

    if not URI:
        raise ValueError("COGNODB_URI is missing from .env")

    if not USERNAME:
        raise ValueError("COGNODB_USERNAME is missing from .env")

    if not PASSWORD:
        raise ValueError("COGNODB_PASSWORD is missing from .env")

    driver = GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD)
    )


def close_driver():
    if driver:
        driver.close()