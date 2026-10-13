class student:
    def __init__(self, name, grades, student_id):
        self.name = name
        self.grades = grades
        self.student_id = student_id

    def get_name(self):
        return self.name

    def get_grades(self):
        return self.grades

    def get_student_id(self):
        return self.student_id

    def display(self):
        print(f"Name: {self.name}, Grades: {self.grades}, Student ID: {self.student_id}")