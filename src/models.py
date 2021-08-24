import dataclasses
from datetime import datetime


@dataclasses.dataclass
class User:
    id: int
    name: str
    email: str
    job_title: str
    created_at: datetime
    updated_at: datetime

    def to_dict(self):
        return dataclasses.asdict(self)
