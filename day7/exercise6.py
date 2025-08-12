class Student:
    school_name = "sands academy"

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, score):
        if 0 <= score <= 100:
            self.grades.append(score)

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def student_info(self):
        avg = self.average_grade()
        return f"{self.name} , {Student.school_name} , Average: {avg:.2f}"


student1 = Student("leen")
student2 = Student("mira")

student1.add_grade(66)
student1.add_grade(80)
student1.add_grade(78)

student2.add_grade(92)
student2.add_grade(88)

print(student1.student_info())
print(student2.student_info())
