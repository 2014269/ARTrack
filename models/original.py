from abc import ABCMeta
from dataclasses import dataclass, field
from models.model import Model
import uuid
from typing import Dict
import datetime


@dataclass(eq=False)
class Original(Model, metaclass=ABCMeta):
    collection: str = field(init=False, default="originals")
    title: str
    medium: str
    dimensions: str
    price: int
    date_created: str
    status: str
    possession: str
    has_prints: str
    is_commission: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {
            "title": self.title,
            "medium": self.medium,
            "dimensions": self.dimensions,
            "price": self.price,
            "date_created": self.date_created,
            "status": self.status,
            "possession": self.possession,
            "has_prints": self.has_prints,
            "is_commission": self.is_commission,
            "_id": self._id
        }
