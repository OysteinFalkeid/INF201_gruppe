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
# Task 0

class Student(ABC):
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        super().__init__()
    @abstractmethod
    def __str__(self):
        #string = 'Name: '+str(self._name)+'\nStudent ID: '+str(self._student_id)
        #return string
        pass

class DataScienceStudent(Student):
    def __init__(self, name : str, student_id : Union[str, int]):
        super().__init__(name, student_id)
    def __str__(self):
        #string = super().__str__()
        string = f"Data Science Student: [{self._student_id}] - [{self._name}]"
        return string
    
class BiologyStudent(Student):
    def __init__(self, name : str, student_id : Union[str, int]):
        super().__init__(name, student_id)
    def __str__(self):
        #string = super().__str__()
        string = f"Biology Student: [{self._name}], ID: [{self._student_id}]"
        return string   

a = BiologyStudent('Eirik', 10)
print(a)
#-------------------------------------------------------------------------------------------------------------------
# Task 1

# msh_name = Path.cwd() / Path('simple.msh')
# msh = meshio.read(msh_name)
# points = msh.points  # mesh points
# cells = msh.cells    # mesh cells
# cell = cells[1].data[222]
# print(cell)
# print(cells[1].type)




