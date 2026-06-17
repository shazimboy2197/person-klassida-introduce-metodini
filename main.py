class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Menim ismim {self.name} va yoshim {self.age}.")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"Men {self.course} kursida o'qiman.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"Men {self.subject} fanidan dars beraman.")

# Test
student = Student("Ali", 20, "Informatika")
student.introduce()

teacher = Teacher("Vali", 35, "Matematika")
teacher.introduce()
