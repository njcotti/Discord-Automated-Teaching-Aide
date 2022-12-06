import random


class AttendanceSystem:
    def __init__(self, Class):
        self._class = Class
        self._generated_code = None

    def generate_code(self):
        self._generated_code = int((random.random() * 10000) // 1)
        return self._generated_code

    def mark_present(self, student_id, code):
        student = self._class.get_student(student_id)
        if code == self._generated_code:
            student.update_attendance()

    def get_attendance(self, student_id):
        student = self._class.get_student(student_id)
        return student.get_attendance()

    def get_class_attendance(self):
        return self._class.get_class_average_attendance()
