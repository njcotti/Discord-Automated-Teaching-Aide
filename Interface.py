from JoinClass import JoinClass
from Class import Class
from AttendanceSystem import AttendanceSystem


class Interface:
    def __init__(self):
        self._class = Class()
        self._system = AttendanceSystem(self._class)
        self._joiner = JoinClass()

    # this class will be the interface that users have access to, hopefully

    # for students
    # AttendanceSystem.sign_up()
    def sign_up(self, name, email, new_id):
        self._joiner.sign_up(name, email, new_id, self._class)

    def mark_present(self, id, code):
        # AttendanceSystem.mark_present()
        self._system.mark_present(id, code)

    def view_attendance(self, student_id):
    # AttendanceSystem.view_attendance()
        return self._system.get_attendance(student_id)
    # AttendanceSystem.change_personal_information

    # for professor
    def take_attendance(self):
        return self._system.generate_code()
    # AttendanceSystem.take_attendance()
    # AttendanceSystem.view_attendance(student_name)
    def view_class_attendance(self):
        return self._system.get_class_attendance()
    # AttendanceSystem.view_class_attendance()
    # way to change office hours
    # way to change office location
    pass
