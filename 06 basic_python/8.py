

# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print('hi, i am ' + self.first_name + ' ' + self.last_name)

class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = []

    def add_grade(self, new_grade):
        self.grades.append(new_grade)

    def salute(self):
        self.greet()
        sum = 0
        for grade in self.grades:
            sum += grade
        print(sum/len(self.grades))

zotyoka = Student("zoli", "kiss")
zotyoka.add_grade(3)
zotyoka.add_grade(4)
zotyoka.add_grade(1)
zotyoka.salute()
