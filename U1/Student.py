class Student:
        """ documentation"""
        course = []
        numberS = 0

        def __init__(self, name, vorname, mtr, course, numberS):
            numberS += 1
            self.name = name
            self.vorname = vorname
            self.mtr = mtr
            self.course = course

        #Ausgabe alles
        def get_details(self):
            return self.__dict__

        #Einschreiben
        def enroll(self, course):
            course.append(self)

        def get_no_of_students(self, numberS):
            return numberS

        def get_course_participants(self, course):
            return course

        #toString
        def __str__(self):
            return f'{self.name}, { self.vorname} , {self.mtr}, {self.course}'


s = Student('Tim', 'Garbe', 7,'', 1)
print(s)

