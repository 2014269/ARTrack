from dataclasses import dataclass, field
from models.model import Model
from abc import ABCMeta
import uuid
from typing import Dict


@dataclass(eq=False)
class Original(Model, metaclass=ABCMeta):
    collection: str = field(init=False, default="contacts")
    name_first: str
    name_last: str
    phone: str
    email: str
    address: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {
            "name_first": self.name_first,
            "name_last": self.name_last,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "_id": self._id
        }
