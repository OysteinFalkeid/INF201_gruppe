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
from typing import Optional

#-------------------------------------------------------------------------------------------------------------------
# Task 2


class Mesh:
    def __init__(self, path: Optional[str] = None):
        self._point = []
        self._cell = []
        if path:
            self.read(path)
        
    def read(self, path: str) -> object:
        msh = meshio.read(path)
        return msh
            

class Point:
    def __init__(self, index: int, x: float, y: float):
        self._index = index
        self._x = 0.0
        self._y = 0.0
        if x and y:
            self._x = x
            self._y = y
        else:
            print('point init missing coordinates')
        

class Cell(ABC):
    def __init__(self, index: int):
        self._index = index
        self._point = []
        super().__init__()
    
    @abstractmethod
    def __str__(self):
        string = 'Index: ' + str(self._index)
        return string
    

class Triangle(Cell):
    def __init__(self, index, point_1, point_2, point_3):
        super().__init__(index)
        self._point = [point_1, point_2, point_3]
    
    def __str__(self):
        string = super().__str__()
        string += f', Points: ({self._point[0]}, {self._point[1]}, {self._point[2]})'
        return string
        
class Line(Cell):
    def __init__(self, index, point_1, point_2):
        super().__init__(index)
        self._point = [point_1, point_2]
    
    def __str__(self):
        string = super().__str__()
        string += f', Points: ({self._point[0]}, {self._point[1]})'
        return string







