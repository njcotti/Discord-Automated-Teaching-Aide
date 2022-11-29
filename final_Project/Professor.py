from User import User


class Professor(User):
    def __init__(self, new_name, new_email, new_id, new_role, office_loc=None, office_hrs=None):
        super().__init__(new_name, new_email, new_id, new_role)
        self._office_location = office_loc
        self._office_hours = office_hrs

    def update_office_hours(self, new_hours):
        # update the list containing office hours
        pass

    def update_office_location(self, new_loc):
        # update the location of the professor's office
        pass
