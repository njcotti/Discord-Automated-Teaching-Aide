import Student
import Professor
import Class

class JoinClass:
    def __init__(self):
        self._no_enrolled = 0

    def sign_up(self, name, email, id, class_object):
        # get the role from class
        role = None
        if self._no_enrolled == 0:
            role = 'professor'
            professor = self.assign_professor(name, email, id, role)
            class_object.set_professor(professor)
        else:
            role = 'student'
            student = self.assign_student(name, email, id, role)
            class_object.add_student(student)

    def assign_student(self, student_name, student_email, student_id, student_role):
        # student needs an id, a name, a role, and an email. Get the role from the class list
        new_student = Student.Student(new_name=student_name, new_email=student_email, new_id=student_id,
                                      new_role=student_role)
        self._no_enrolled = self._no_enrolled + 1
        return new_student

    def assign_professor(self, professor_name, email, id, role, office_hours=None, office_location=None):
        # professor needs at least a name, email, id, and a role (professor). Get the role from length of class_roll
        professor = Professor.Professor(new_name=professor_name, new_email=email, new_id=id, new_role=role)
        self._no_enrolled = self._no_enrolled + 1
        return professor
