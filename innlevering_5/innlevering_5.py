# innlevering 5

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
# This is the last introductory exercise sheet. 
# Starting next week, we will move to the project part of the exercises. 
# Work on exercise 5 together with your partner. 
# Do not share your code with other groups. 
# Use VSCode, virtual environments, and a "requirements.txt" file to install and document packages. 
# Only one person in the group hands in the assignment. 
# If you are the person to submit your solution, send a screenshot of the submission notification 
# to your partner so that both of you know the exercise has been submitted. 
# Indicate both your names and NMBU email addresses on top of your .py file or your notebook. 
# Only share code with your project partner. 
# Persons who hand in alone will not receive points unless we see that they have actively 
# tried to find a partner by adding their name to the Padlet (https://padlet.com/jonaskusch1/exerciseteams2024Links to an external site.) 
# before Tuesday, October 8th.  Use the concepts learned in this course to solve the assignment.

# Upload your solution before Monday at 2 pm as a Python file or Jupyter Notebook. 
# In addition, if you are using a .py file, upload a .txt file with the output of your code. 
# In case you are using a Jupyter Notebook, generate an output pdf and hand it in. 
# Your points will then be uploaded to Canvas. You cannot submit this exercise multiple times. 
# Exercises that give 0 points are meant to help you or provide a deeper understanding. 
# Since they do not give points, you do not have to solve them, but they will help you become a good programmer. 
# Moreover, if you are unfamiliar with matrices, vectors, and simple matrix-vector operations, you can look at this help assignment.

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

# Task 0: Warmup exercise (0 points)

#-------------------------------------------------------------------------------------------------------------------
print('Task 0: Warmup exercise (0 points)')
print()

def inplace_add_vectors(vec1: list[Union[int, float]] = [], vec2: list[Union[int, float]] = []) -> None:
    if len(vec1) == len(vec2):
        for i in range(len(vec1)):
            vec1[i] = vec1[i] + vec2[i]
    else:
        print('vectors of diferent length')

def add_vectors(vec1: list[Union[int, float]] = [], vec2: list[Union[int, float]] = []) -> Optional[list[Union[int, float]]]:
    if len(vec1) == len(vec2):
        vec3 = vec1.copy()
        for i in range(len(vec1)):
            vec3[i] = vec1[i] + vec2[i]
        return vec3
    else:
        print('vectors of diferent length')
        return None
    
print('1 Define a function called inplace_add_vectors(vec1, vec2):')
vector1 = [1,2,3]
vector2 = [4,5,6]
inplace_add_vectors(vector1, vector2)
print(vector1)
print()

print('2 Define a function called add_vectors(vec1, vec2):')
vector1 = [1,2,3]
vector2 = [4,5,6]
vector3 = add_vectors(vector1, vector2)
print(vector1)
print(vector3)
print()

print('------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------

# Task 1: Matrix operations (2 points)

#-------------------------------------------------------------------------------------------------------------------
print('Task 1: Matrix operations (2 points)')
print()

shape = (5000, 5000)
matrix = np.random.randint(0, 100, shape)

def mean(matr: list[list[Union[int, float]]]) -> Union[int, float]:
    return sum(matr) / (len(matr)**2)

def variance(matr: list[list[Union[int, float]]]) -> Union[int, float]:
    sum = 0.0
    mean_value = mean(matr)
    for row in matr:
        for col in row:
            sum += (float(col)-mean_value)**2
    return sum / (len(matr)**2)
    
def sum(matr: list[list[Union[int, float]]]) -> Union[int, float]:
    sum = 0
    for row in matr:
        for col in row:
            sum += col
    return sum

def multiply(matr: list[list[Union[int, float]]], val: Union[int, float]) -> list[list[Union[int, float]]]:
    mul_matr = matr.copy()
    for i, row in enumerate(matr):
        for j, col in enumerate(row):
            mul_matr[i][j] = col * val
    return mul_matr
            

print(f'the mean value is: {mean(matrix)}')
print()
print('the matrix multiplied is:')
print(np.asarray(multiply(matrix, 2)))
print()
print(f'the variance is: {variance(matrix)} \nand this value is equivalent to the numpy variance: {np.var(matrix)}')


print('------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------

# Task 2: Stencil matrix (3 points)

#-------------------------------------------------------------------------------------------------------------------
print('Task 2: Stencil matrix (3 points)')
print()

shape = 50
matrix = [[0 for i in range(shape)] for j in range(shape)]

for i in range(shape):
    for j in range(shape):
        if i is j:
            matrix[i][j] = -2
        elif j-1 is i or j+1 is i:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0
            
matrix = np.asarray(matrix)
vector = np.random.rand(shape)

for i in range(100):
    vector = np.dot(matrix, vector)/np.linalg.norm(vector)

eigenvalue = abs(np.dot(np.transpose(vector), np.dot(matrix, vector))/np.dot(np.transpose(vector), vector))
Lambda, V = np.linalg.eig(matrix)

print(f'eigenvalue calculated with for loop is: {eigenvalue} \nand the eigenvalue calculated with numpy is: {max(abs(Lambda))}')

print('------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------

# Task 3: Challenge exercise (0 points)

#-------------------------------------------------------------------------------------------------------------------
print('Task 3: Challenge exercise (0 points)')
print()








print('------------------------------------------------------------------------')
