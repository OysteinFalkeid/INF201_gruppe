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
        '''
        Creates a class containing lists of points and cells.
        The class has a read function that reads from .msh file if path exists
        
        Args:
            path (str): The path to the .msh file containing the mesh
            
        Examples:
            >>> Mesh(my/path.msh)
            object containing lists based on my/path.msh
            >>> Mesh()
            Emptey object
        '''
        self._points = []
        self._cells = []
        if path:
            self.mesh = self.read(path)
        
    def read(self, path: str) -> object:
        '''
        Reads from file at path. Saves file content as lists.
        
        Args:
            path (str): The path to the .msh file containing the mesh
            
        Examples:
            >>> read(my/path.msh)
            Saves file content as lists at points and cells
        '''
        msh = meshio.read(path)
        
        for point in msh.points:
            pass
        return msh
    
    @property
    def points(self):
        return self._points
    
    @property
    def cells(self):
        return self._cells

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
    
    @property
    def index(self):
        return self._index
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
        

class Cell(ABC):
    def __init__(self, index: int):
        super().__init__()
        self._index = index
        self._points = []
    
    @abstractmethod
    def __str__(self):
        string = 'Index: ' + str(self._index)
        return string
    
    @property
    def index(self):
        return self._index
    
    @property
    def points(self):
        return self._points
    

class Triangle(Cell):
    def __init__(self, index, point_1, point_2, point_3):
        super().__init__(index)
        self._points = [point_1, point_2, point_3]
    
    def __str__(self):
        string = super().__str__()
        string += f', Points: ({self._point[0]}, {self._point[1]}, {self._point[2]})'
        return string
        
class Line(Cell):
    def __init__(self, index, point_1, point_2):
        super().__init__(index)
        self._points = [point_1, point_2]
    
    def __str__(self):
        string = super().__str__()
        string += f', Points: ({self._point[0]}, {self._point[1]})'
        return string

trekant = Triangle(1, 1, 2, 3)

path = Path.cwd() / Path('simple.msh')
mesh = meshio.read(path)
print(mesh)
