# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student():
  def __init__(self):
    self.grades = []

  def add_grade(self, grade):
    if grade > 0 and grade < 6 and type(grade) == int:
      self.grades.append(grade)

  def sum_of_grades(self):
    sum = 0
    for grade in self.grades:
      sum += grade
    return sum

  def get_average(self):
    if len(self.grades) > 0:
      return self.sum_of_grades() / len(self.grades)

student1 = Student()

student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(2)
student1.add_grade(4)
student1.add_grade(4)

print(student1.grades)
print(student1.get_average())
