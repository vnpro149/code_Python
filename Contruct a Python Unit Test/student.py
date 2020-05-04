import subject


class Student:
    def __init__(self, name):
        self.name = name
        self.email = None
        self.subjects = []
        self.grades = []

    def add_subject(self, subject):
        if subject:
            if subject not in self.subjects:
                self.subjects.append(subject)
                return True
            else:
                return False
        else:
            return False

    def set_grade(self, subject, grade):
        if (subject and grade) or (subject and grade is int(0)):
            if subject in self.subjects:
                if grade < 1 or grade > 10:
                    raise ValueError('grade out of bound', grade)
                else:
                    self.grades.append((subject, grade))
                    return True

            else:
                raise ValueError('no subject or grade', subject)
        else:
            return False

    def get_grades_for_subject(self, subject):
        if subject:
            grades = []
            for grade in self.grades:
                if grade[0] is subject:
                    grades.append(grade[1])
        else:
            return False

        return grades
