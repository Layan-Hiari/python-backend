class Person:
    def init(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Email: {self.email}")

    def get_email(self):
        return self.email

    def repr(self):
        return f"Person({self.id!r}, {self.name!r}, {self.email!r})"


class Student(Person):
    def init(self, id, name, email, major, gpa):
        super().init(id, name, email)
        self.major = major
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def lt(self, other):
        return self.gpa < other.gpa

    def repr(self):
        return f"Student({self.id!r}, {self.name!r}, GPA={self.gpa!r})"


class Professor(Person):
    def init(self, id, name, email, department):
        super().init(id, name, email)
        self.department = department
        self.courses_teaching = []

    def add_course(self, course):
        self.courses_teaching.append(course)
#lt → < compares GPAs between students.
#repr__ → debug-friendly string showing object details.