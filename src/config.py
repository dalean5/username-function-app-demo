import os
from urllib import parse


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5432")
    password = os.environ.get("DB_PASSWORD", "password")
    user = os.environ.get("DB_USER", "user")
    db = os.environ.get("DB_NAME", "db")

    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


# print(get_postgres_uri())
