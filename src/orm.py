from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    DateTime,
    func,
)
from sqlalchemy.orm import registry

from .models import User

mapper_registry = registry()

metadata = MetaData()

users_table = Table(
    "serverless_users",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String(60), nullable=False),
    Column("email", String(255), nullable=False),
    Column("job_title", String(255), nullable=False),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
)


def start_mappers():
    mapper_registry.map_imperatively(User, users_table)
