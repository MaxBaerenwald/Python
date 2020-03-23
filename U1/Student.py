class Student:
        """ documentation"""
        course = ["Mathe", "Prog", "OOSS",]
        numberS = 0

        def __init__(self, name, vorname, mtr, course):
            self.name = name
            self.vorname = vorname
            self.mtr = mtr
            self.course = course

        def get_details(self):
            return self

        def enroll(self, course):
            return

        def get_no_of_students(self, numberS):
            numberS += 1
            return

        def get_course_participants(self, course):
            return

        def __str__(self):
            return
