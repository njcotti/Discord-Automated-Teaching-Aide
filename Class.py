
class Class:
    def __init__(self):
        self._attendance_avg = 0.00

        # professor of type professor
        self._professor = None

        # Class roll should be a list of Students
        self._class_roll = []

    def add_student(self, new_student):
        # will need to make a new comparator?
        if new_student not in self._class_roll:
            self._class_roll.append(new_student)

    # searches the class roll for a student matching the name, return none if none
    def get_student(self, student_id):
        for student in self._class_roll:
            if student.get_id() == student_id:
                return student
        return None

    def get_enrollment_numbers(self):
        return len(self._class_roll)

    def set_professor(self, new_professor):
        self._professor = new_professor

    def calculate_average_attendance(self):
        revised_average = 0
        sum_of_ratios = 0.0
        for student in self._class_roll:
            sum_of_ratios = sum_of_ratios + student.get_attendance()
        revised_average = sum_of_ratios / len(self._class_roll)
        return revised_average

    def get_class_average_attendance(self):
        self._attendance_avg = self.calculate_average_attendance()
        return self._attendance_avg
