import json
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import sessionmaker, clear_mappers

import azure.functions as func

from src.orm import start_mappers
from src.config import get_postgres_uri
from src.serializers import JsonUserSerializer
from src.repo import PostgresRepository

get_session = sessionmaker(bind=create_engine(get_postgres_uri()))
session = get_session()
repo = PostgresRepository(session=session)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    user_id = req.route_params.get("id")

    # if the request is valid, persist to the database

    # build user object and add to database
    try:
        start_mappers()
        retrieved_user = repo.get(user_id)
        return func.HttpResponse(
            body=json.dumps(retrieved_user, cls=JsonUserSerializer),
            mimetype="application/json",
            status_code=200,
        )
    except NoResultFound:
        return func.HttpResponse(mimetype="application/json", status_code=404)
    finally:
        clear_mappers()
