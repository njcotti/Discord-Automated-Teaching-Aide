

class User:
    def __init__(self, new_name, new_email, new_id, new_role):
        self._name = new_name
        self._email = new_email
        self._discord_id = new_id
        self._role = new_role

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_role(self):
        return self._role
