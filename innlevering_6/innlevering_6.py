# innlevering 6

# Group members:

# Oystein Falkeid
# e-mail: oystein.falkeid@nmbu.no

# Eirik Mentyjaervi
# e-mail: eirik.mentyjarvi@nmbu.no

import sys
from pathlib import Path

#printer til fil i stedenfor terminal
file = Path('.') / Path('terminal.txt')
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

print('------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------
 
# Task 0: Warmup Exercise (0 points)

#-------------------------------------------------------------------------------------------------------------------
print('Task 0: Warmup Exercise (0 points)')
print()

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def make_sound(self) -> None:
        print(f'the {self.name} makes a sound')

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed
    
    def make_sound(self) -> None:
        print(f'the {self.breed} barks')
        
class Cat(Animal):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color
        
    def make_sound(self):
        print(f'The {self.color} cat meows')

pluto = Dog('Pluto', 12, 'labradoodle')
garfeeld = Cat('Garfeeld', 9, 'orange')

pluto.make_sound()
garfeeld.make_sound()

print('------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------

# Task 1: University System Simulation (10 points)
# In this exercise, you will design and implement a simple university system using object-oriented programming (OOP) principles in Python. You will build a system where students enroll in courses, teachers assign grades, and courses track their enrolled students. 

# Part 1: Core Class Structure
# In the first part of the exercise, you will focus on creating the core classes and implementing basic functionality.

# Step 1: Create the Person Class
# Create a base class called Person. This class will serve as the foundation for other types of people at the university (e.g., students and teachers).
# Person should have the following attributes (member variables):
# _name: The person's name.
# _age: The person's age.
# _email: The person's email address.
# Implement a method get_details() that returns a string containing the person’s information in the format: Name: <name>, Age: <age>, Email: <email>.
# Step 2: Create Derived Classes Student and Teacher
# Next, you will create two classes that inherit from Person: Student and Teacher.

# Student:

# Inherit from Person.
# Add a member variable _student_id to store the student's ID.
# Add a member variable _courses (a list) to store the courses the student is enrolled in.
# Create a method enroll_in_course(course) that allows a student to enroll in a course by adding the course to the courses list.
# Teacher:

# Inherit from Person.
# Add a member variable subject to store the subject the teacher teaches.
# Implement a method assign_grade(student, grade) that prints a message indicating the grade assigned to the student by the teacher. You will add more functionality to this method in Part 2 of this exercise.
# Step 3: Create the Course Class
# Define a Course class that will represent a university course.
# The class should have the following attributes:
# _course_name: The name of the course.
# _course_code: The course's unique code (e.g., "INF201").
# _enrolled_students: A list that stores all the students enrolled in the course.
# Implement a method add_student(student) to enroll a student in the course. This should add the student to the enrolled_students list and also enroll the student in the course by calling their enroll_in_course(course) method.
# Create a method list_students() that returns a list of all students enrolled in the course (calling each student’s get_details() method).
# Part 2: Adding Advanced Features
# In the second part of the exercise, you will extend the functionality of the Student and Teacher classes and make the interactions between classes more dynamic.

# Step 4: Add Grade Management
# Modify the Student class to store a dictionary of grades for each course.

# Add a member variable grades (a dictionary) where keys are course names and values are grades.
# Implement a method assign_grade(course, grade) that allows a student to store the grade they received for a course in the grades dictionary.
# Create a method get_grades() that returns the dictionary of courses and grades.
# Update the Teacher class so that the assign_grade() method assigns grades to students by calling their assign_grade(course, grade) method, rather than just printing a message.

# Step 5: Test the System
# Simulate a real-world scenario by creating instances of Teacher, Student, and Course. Implement the following functionality:

# Create a few Student objects and a Teacher object.
# Create at least one Course and enroll students in the course.
# Use the Teacher class to assign grades to students for the course.
# Have students check their grades by calling their get_grades() method.
# List all the students enrolled in the course by using the list_students() method.
 
#-------------------------------------------------------------------------------------------------------------------
print('Task 1: University System Simulation (10 points)')
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


print('------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------