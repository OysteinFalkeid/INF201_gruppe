# innlevering 6

# Group members:

# Oystein Falkeid
# e-mail: oystein.falkeid@nmbu.no

# Eirik Mentyjaervi
# e-mail: eirik.mentyjarvi@nmbu.no

import sys
from pathlib import Path

#printer til fil i stedenfor terminal
file = Path.cwd() / Path('terminal.txt')
sys.stdout = open(file, 'w')

print('innlevering 5')
print()

# How to work on this exercise
# This is the first project exercise sheet. Work on exercise 6 together with your partner. Do not share your code with other groups. Use VSCode, virtual environments, and a "requirements.txt" file to install and document packages. Only one person in the group hands in the assignment. If you are the person to submit your solution, send a screenshot of the submission notification to your partner so that both of you know the exercise has been submitted. Indicate both your names and NMBU email addresses on top of your .py file or your notebook. Only share code with your project partner. Persons who hand in alone will not receive points unless we see that they have actively tried to find a partner by adding their name to the Padlet (https://padlet.com/jonaskusch1/exerciseteams2024Links to an external site.) before or on Tuesday, October 15th.  Use the concepts learned in this course to solve the assignment.

# Upload your solution before Monday at 2 pm on October 28th as a Python file or Jupyter Notebook. In addition, if you are using a .py file, upload a .txt file with the output of your code. If you are using a Jupyter Notebook, generate an output pdf and hand it in. You can submit this exercise multiple times, and your last submission will be graded. Submit your exercise via the submission groups! Do not submit this exercise as an individual assignment.

#-------------------------------------------------------------------------------------------------------------------
print('Group members:')
print()
# Group members

print('Oystein Falkeid')
print('e-mail: oystein.falkeid@nmbu.no')
print()
print('Eirik Mentyjaervi')
print('e-mail: eirik.mentyjarvi@nmbu.no')   
print()                  

import numpy as np # henter numpy til å brukes i oppgavene
from typing import Union
from typing import Optional
from random import randint

print('------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------
 
# Task 0: Warmup Exercise (0 points)

#-------------------------------------------------------------------------------------------------------------------
print('Task 0: Warmup Exercise (0 points)')
print()

class Animal:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        
    def make_sound(self) -> None:
        print(f'the {self._name} makes a sound')

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self._breed = breed
    
    def make_sound(self) -> None:
        print(f'the {self._breed} barks')
        
class Cat(Animal):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self._color = color
        
    def make_sound(self):
        print(f'The {self._color} cat meows')

pluto = Dog('Pluto', 12, 'labradoodle')
garfeeld = Cat('Garfeeld', 9, 'orange')

pluto.make_sound()
garfeeld.make_sound()

print('------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------

# Task 1: University System Simulation (10 points)
 
#-------------------------------------------------------------------------------------------------------------------
print('Task 1: University System Simulation (10 points)')
print()

type person_class = Person
type teacher_class = Teacher
type student_class = Student
type course_class = Course

# Step 1: Create the Person Class
class Person:
    def __init__(self, name: str, age: int,email: str) -> None:
        self._name = name
        self._age = age
        self._email = email
    
    def __str__(self) -> str:
        return (f'Name: {self._name}, Age: {self._age}, Email: {self._email}')
    
    def get_details(self) -> str:
        return (f'Name: {self._name}, Age: {self._age}, Email: {self._email}')

#Step 2: Create Derived Classes Student and Teacher
class Student(Person):
    def __init__(self, name: str, age: int, email: str, id: str, courses: Optional[list[str]] = None) -> None:
        super().__init__(name, age, email)
        self._student_id = id
        if courses:
            self._courses = courses
        else:
            self._courses = []
        #Step 4: Add Grade Management
        self._grades = {}
    
    def enroll_in_course(self, course: str) -> None:
        if course not in self._courses:
            self._courses.append(course)
            print(f'student { self._name} hase enroled to {course}')
        else:
            print(f'course {course} alreaddy in list')
    
    #Step 4: Add Grade Management 
    def assign_grade(self, course: str, grade: int) -> None:
        self._grades[course] = grade
    
    #Step 4: Add Grade Management
    def get_grades(self) -> dict:
        return self._grades
    
    def __str__(self):
        string = super().__str__()
        string += (f', Student ID: {self._student_id}')
        return string

class Teacher(Person):
    def __init__(self, name: str, age: int, email: str, subject: str) -> None:
        super().__init__(name, age, email)
        self._subject = subject
    
    #Step 4: Add Grade Management
    def assign_grade(self, student: student_class, course: str, grade: int) -> None:
        student.assign_grade(course, grade)

#Step 3: Create the Course Class
class Course:
    def __init__(self, name: str, code: int, enrolled_students: Optional[list[student_class]] = None) -> None:
        self._course_name = name
        self._course_code = code
        if enrolled_students:
            self._enrolled_students = enrolled_students
        else:
            self._enrolled_students = []
        
    def add_student(self, student: student_class) -> None:
        if student not in self._enrolled_students:
            self._enrolled_students.append(student)
            student.enroll_in_course(self._course_code)
        else:
            print('student alreaddy enroled')
            
    def list_students(self) -> None:
            for student in self._enrolled_students:
                print(student)

#Step 5: Test the System  
#Create a few Student objects and a Teacher object.            
teacher_1 = Teacher(name='teacher_1', age=6, email='teacher_1@nmbu.no', subject='programering')

student_1 = Student(name='student_1', age=1, email='student_1@nmbu.no', id=1)
student_2 = Student(name='student_2', age=2, email='student_2@nmbu.no', id=2)
student_3 = Student(name='student_3', age=3, email='student_3@nmbu.no', id=3)
student_4 = Student(name='student_4', age=4, email='student_4@nmbu.no', id=4)
student_5 = Student(name='student_5', age=5, email='student_5@nmbu.no', id=5)
students = [student_1, student_2, student_3, student_4, student_5]

#Create at least one Course and enroll students in the course.
course_1 = Course(name='programering', code=201)

for student in students:
    course_1.add_student(student)
print()

for student in students: 
    #Use the Teacher class to assign grades to students for the course.
    teacher_1.assign_grade(student=student, course='programering', grade=randint(1, 6))
    
    #Have students check their grades by calling their get_grades() method.
    print(student.get_grades())
print()

#List all the students enrolled in the course by using the list_students() method.
course_1.list_students()

print()
print('------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------

# Task 2: Challenge assignment (0 points)
# Implement a single layer neural network. That is, implement 
#  where 
#  are called the weights, 
#  is the input (this can contain the pixels of a 8 by 8 pixel image, that is, 
# ), and 
#  is the bias. The function 
#  applies the so-called reluLinks to an external site. function element-wise. That is, for a scalar 
#  we have 
#  if 
#  and 
#  if 
# . Or in less mathematical terms, make sure that 
#  is a data array with 
#  rows and 
#  columns, 
#  is a data vector with 
#  entries, and 
#  is a data vector with 
#  entries. 
# Extend the neural network to a second layer, i.e., use the output of the first layer as input to a second layer 
# , where 
# , and 
# .
# Repeat this process for a given and variable number of L layers. The dimensions of all layers should be defined in a vector 
# . Make sure your program does not modify the input 
#  when computing the response of your neural network.
# Print the output of your program 
#  (which is the output of the neural network) as well as the dimensions of all weight matrices for 
# . For now, random numbers should be used in all matrices and vectors that require initialization. In the future, we will choose the pixels of the MNIST datasetLinks to an external site. as 
#  and pick trained and meaningful weights and biases so that your network will be able to recognize the number in your image.
 
#-------------------------------------------------------------------------------------------------------------------
print('Task 2: Challenge assignment (0 points)')
print()


class Layer:
    def __init__(self, matrix = None, vector = None, y = [], x = []):
        if matrix:
            self._M = matrix
        else:
            self.set_random_value_M()
        
        if vector:
            self._B = vector
        else:
            self.set_random_value_B()

        self._y = y
        self._x = x
        
        def _sigma(y):
            return y
        self._sigma_vec = np.vectorize(_sigma)
    
    def output(self, x) -> np.ndarray:
        return self._sigma_vec(self._M @ x + self._B)
    
    def set_M(self, M):
        self._M = M
        
    def set_B(self, B):
        self._B = B
        
    def set_variables(self, M, B, y = None):
        self.set_M(M)
        self.set_B(B)
        if y:
            self._y = y
    
    def set_random_value_M(self, shape = (8,8)):
        self.set_M(np.random.rand(shape[0], shape[1]))
    
    def set_random_value_B(self, shape = 8):
        self.set_B(np.random.rand(shape))
    
    def set_random_values(self, shape = (8,8)):
        self.set_random_value_M(shape)
        self.set_random_value_B(shape[0])
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
        
    def calculate_x(self, x = None):
        if x is not None:
            self._x = x
        elif self._x is [] and self._y is []:
            self._x = self._y
            
        self._y = self.output(x=self._x)
        
x = np.random.rand(64)
layer = Layer(x=x)
layer.set_random_value_M((8,64))
layer.calculate_x()

for layers in range(10):
    layer.set_random_values()
    layer.calculate_x(x=layer.get_y())
    
print(layer.get_x())


print('------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------