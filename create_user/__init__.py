import json
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

import azure.functions as func

from src.orm import start_mappers
from src.models import User
from src.config import get_postgres_uri
from src.repo import PostgresRepository

get_session = sessionmaker(bind=create_engine(get_postgres_uri()))
session = get_session()
repo = PostgresRepository(session=session)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    req_body = req.get_json()

    # very simple and naive req_body validation
    if req_body.get("name") is None or req_body.get("name") == "":
        return func.HttpResponse(
            body=json.dumps({"error": "name must be present in request body"}),
            mimetype="application/json",
            status_code=400,
        )
    if req_body.get("email") is None or req_body.get("email") == "":
        return func.HttpResponse(
            body=json.dumps({"error": "email must be present in request body"}),
            mimetype="application/json",
            status_code=400,
        )
    if req_body.get("job_title") is None or req_body.get("job_title") == "":
        return func.HttpResponse(
            body=json.dumps({"error": "job_title must be present in request body"}),
            mimetype="application/json",
            status_code=400,
        )

    # if the request is valid, persist to the database

    # build user object and add to database
    try:
        start_mappers()
        repo.add(
            User(
                id=None,
                name=req_body["name"],
                email=req_body["email"],
                job_title=req_body["job_title"],
                created_at=None,
                updated_at=None,
            )
        )
        session.commit()
        return func.HttpResponse(mimetype="application/json", status_code=201)
    except Exception:
        return func.HttpResponse(status_code=400, mimetype="application/json")
    finally:
        clear_mappers()
