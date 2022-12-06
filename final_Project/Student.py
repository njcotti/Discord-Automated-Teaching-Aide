from User import User


class Student(User):
    def __init__(self, new_name, new_email, new_id, new_role):
        # call super class User and construct a user.
        super().__init__(new_name, new_email, new_id, new_role)
        # all attendances should initialize to 0.
        self._attendance_percent = 0.00
        self._total_attended = 0
        self._total_days = 0

    # return the attendance from 0.00 to 1.00
    def get_attendance(self):
        return self._attendance_percent

    def get_id(self):
        return self._discord_id

    def update_attendance(self):
        self._total_days = self._total_days + 1
        self._total_attended = self._total_attended + 1
        self._attendance_percent = self._total_attended / self._total_days
