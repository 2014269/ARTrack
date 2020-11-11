from abc import ABCMeta
from dataclasses import dataclass, field
from models.model import Model
from models.contact import Contact
import uuid
from typing import Dict
import datetime
from models.user import User


@dataclass(eq=False)
class Original(Model, metaclass=ABCMeta):
    collection: str = field(init=False, default="originals")
    title: str
    medium: str
    dimensions: str
    price: int
    date_created: str
    status: str
    possession: str # "David Greaves"
    has_prints: str
    is_commission: str
    user_email: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
        self.user = User.find_by_email(self.user_email)
        # try:
        #     self.possession_contact = Contact.get_by_full_name(self.possession)
        #
        # except:
        #     self.possession_contact = None

    def json(self) -> Dict:
        return {
            "title": self.title,
            "medium": self.medium,
            "dimensions": self.dimensions,
            "price": self.price,
            "date_created": self.date_created,
            "status": self.status,
            "possession": self.possession,
            # "possession_contact": self.possession_contact,
            "has_prints": self.has_prints,
            "is_commission": self.is_commission,
            "user_email": self.user_email,
            "_id": self._id
        }
