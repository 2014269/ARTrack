import re

class Utils:

    @staticmethod
    def email_is_valid(email: str) -> bool:
        # credit: emailregex.com
        email_address_matcher = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        return True if email_address_matcher.match(email) else False

