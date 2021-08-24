import json

from .models import User


class JsonUserSerializer(json.JSONEncoder):
    def default(self, o: User):
        try:
            to_serialize = {
                "id": o.id,
                "name": o.name,
                "email": o.email,
                "job_title": o.job_title,
                "created_at": o.created_at.isoformat(),
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
