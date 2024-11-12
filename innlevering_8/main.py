# innlevering 8

# Group members:

# Oystein Falkeid
# e-mail: oystein.falkeid@nmbu.no

# Eirik Mentyjaervi
# e-mail: eirik.mentyjarvi@nmbu.no

import sys
from pathlib import Path

#printer til fil i stedenfor terminal
file = Path.cwd() / Path('terminal.txt')
sys.stdout = open(file, 'w',encoding='utf-8')

print('innlevering 6')
print()

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

import meshio
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Optional, Union


#-------------------------------------------------------------------------------------------------------------------
# Task 0 DONE

# class Student(ABC):
#     def __init__(self, name, student_id):
#         self._name = name
#         self._student_id = student_id
#         super().__init__()
#     @abstractmethod
#     def __str__(self):
#         #string = 'Name: '+str(self._name)+'\nStudent ID: '+str(self._student_id)
#         #return string
#         pass

# class DataScienceStudent(Student):
#     def __init__(self, name : str, student_id : Union[str, int]):
#         super().__init__(name, student_id)
#     def __str__(self):
#         #string = super().__str__()
#         string = f"Data Science Student: [{self._student_id}] - [{self._name}]"
#         return string
    
# class BiologyStudent(Student):
#     def __init__(self, name : str, student_id : Union[str, int]):
#         super().__init__(name, student_id)
#     def __str__(self):
#         #string = super().__str__()
#         string = f"Biology Student: [{self._name}], ID: [{self._student_id}]"
#         return string   

# class StudentFactory:
#     def __init__(self):
#         #self._student_types = {"ds": DataScienceStudent, "bio": BiologyStudent}
#         self._student_types = {}
#     def register(self, key, student_class):
#         self._student_types[key] = student_class
#     def __call__(self, key, name, student_id):
#         if key not in self._student_types:
#             return f"Student type {key} not registered"
#         else:
#             return self._student_types[key](name, student_id)
    
# factory = StudentFactory()

# factory.register("ds", DataScienceStudent)
# factory.register("bio", BiologyStudent)

# student0 = factory("ds", "Eirik", 100)
# student1 = factory("bio", "Mathias", 101)

# print(student0)
# print(student1)

#-------------------------------------------------------------------------------------------------------------------
# Task 0 EXPERIMENTAL

class Student(ABC):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    @abstractmethod
    def __str__(self):
        return f"Name: {self.name}, StudentID: {self.student_id}"
    
class DataScienceStudent(Student):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
    def __str__(self):
        string = super().__str__()
        string += f", Course: Data Science"
        return string

class BiologyStudent(Student):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
    def __str__(self):
        string = super().__str__()
        string += f", Course: Biology"
        return string

class StudentFactory:
    def __init__(self):
        self.student_types = {}
    def register(self, key, student_class):
        self.student_types[key] = student_class
    def __call__(self, key, name, student_id):
        if key not in self.student_types:
            return f"Error: {key} not in registry"
        else:
            return self.student_types[key](name, student_id)

fac = StudentFactory()
fac.register("ds", DataScienceStudent)
fac.register("bio", BiologyStudent)

student0 = fac("ds", "Eirik", 10)

print(student0)

#-------------------------------------------------------------------------------------------------------------------
# Task 1

# msh_name = Path.cwd() / Path('simple.msh')
# msh = meshio.read(msh_name)
# points = msh.points  # mesh points
# cells = msh.cells    # mesh cells
# cell = cells[1].data[222]
# print(cell)
# print(cells[1].type)




