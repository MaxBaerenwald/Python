class Student(object):
    '''
    Student Class
    '''
    courses = {}
    count = 0

    def __init__(self, mat_nr, name, first_name):
        self.mat_nr = mat_nr
        self.name = name
        self.first_name = first_name
        Student.count += 1

    def get_details(self):
        return self.mat_nr, self.name, self.first_name

    def enroll(self, course):
        if course in self.courses:
            self.courses[course].append(self)
        else:
            self.courses[course] = [self]

    @staticmethod
    def get_no_of_students():
        return Student.count

    def get_course_participants(self, course):
        if course in self.courses:
            return self.courses[course]

    def __str__(self) -> str:
        output = f'Student: mat_nr: {self.mat_nr}, {self.first_name} {self.name}, courses:'
        courses = self.courses.keys()
        for course in courses:
            if self in self.courses[course]:
                output += course
        return output


tim = Student(20200001, 'Test', 'Tim')
mat_nr, name, first_name = tim.get_details()
print(f'mat_nr: {mat_nr}, name: {name}, first_name: {first_name}')
tim.enroll('OOSL')
print(tim)

print(f'get_no_of_students: {Student.get_no_of_students()}')

max_mustermann = Student(20200000, 'Mustermann', 'Max')
max_mustermann.enroll('OOSL')

print(f'get_no_of_students: {Student.get_no_of_students()}')

print('OOSL:')
for student in tim.get_course_participants('OOSL'):
    print(student)