from typing import List

from .models import User


class PostgresRepository:
    def __init__(self, session):
        self.session = session

    def add(self, user: User):
        self.session.add(user)

    def get(self, id: int) -> User:
        return self.session.query(User).filter_by(id=id).one()

    def list(self) -> List[User]:
        return self.session.query(User).all()
