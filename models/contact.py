from dataclasses import dataclass, field
from models.model import Model
from abc import ABCMeta
import uuid
from typing import List, Dict, TypeVar, Type


@dataclass(eq=False)
class Contact(Model, metaclass=ABCMeta):
    collection: str = field(init=False, default="contacts")
    name_first: str
    name_last: str
    phone: str
    email: str
    address: str
    user_email: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    # def __post_init__(self):
    #     self.name_full = self.name_first + " " + self.name_last

    def json(self) -> Dict:
        return {
            "name_first": self.name_first,
            "name_last": self.name_last,
            # "name_full": self.name_full,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "user_email": self.user_email,
            "_id": self._id
        }

    # @classmethod
    # def get_by_full_name(cls: "Contact", name_full: str) -> "Contact":
    #     return cls.find_one_by("name_full", name_full)

