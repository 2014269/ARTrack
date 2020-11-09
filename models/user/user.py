from dataclasses import dataclass, field
from models.model import Model
from abc import ABCMeta
import uuid
from typing import Dict, List
from common.database import Database
from common.utils import Utils
import models.user.errors as UserErrors


@dataclass(eq=False)
class User(Model, metaclass=ABCMeta):
    collection: str = field(init=False, default="users")
    # name_first: str
    # name_last: str
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {
            # "name_first": self.name_first,
            # "name_last": self.name_last,
            "email": self.email,
            "password": self.password,
            "_id": self._id
        }

    @classmethod
    def find_by_email(cls, email: str) -> "User":
        try:
            return cls.find_one_by('email', email)
        except TypeError:
            raise UserErrors.UserNotFoundError('A user with this email was not found')

    @classmethod
    def register_user(cls, email: str, password: str) -> bool:
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError('The email does not have the right format')

        try:
            user = cls.find_by_email(email)
            raise UserErrors.UserAlreadyRegisteredError('The email you used to register already exists')
        except UserErrors.UserNotFoundError:
            User(email, Utils.hash_password(password)).save_to_mongo()

        return True

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> "User":
        user = cls.find_by_email(email)

        if not Utils.check_hashed_password(password, user.password):
            raise UserErrors.IncorrectPasswordError('Your password')

        return True
