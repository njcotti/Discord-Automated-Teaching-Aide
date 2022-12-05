

class Class:
    def __init__(self, new_professor):
        self._attendance_avg = 0.00

        # professor of type professor
        self._professor = new_professor

        # Class roll should be a list of Students
        self._class_roll = []

    def add_student(self, new_student):
        # will need to make a new comparator?
        if new_student not in self._class_roll:
            self._class_roll.append(new_student)

    # searches the class roll for a student matching the name, return none if none
    def get_student(self, student_name):
        for student in self._class_roll:
            if student.getName() is student_name:
                return student
        return None
