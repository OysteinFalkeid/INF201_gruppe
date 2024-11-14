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

print('innlevering 8')
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

class Mesh_object(ABC):
    def __init__(self, index: int):
        '''
        Abstract class for objects in a mesh. 
        
        The objects can be points or cells
        '''
        super().__init__()
        self._index = index
        
    @property
    def index(self):
        '''
        Returns the index of the mesh object
        
        Points and cells have indexes starting from 1.
        Meaning point 1 and cell 1 can exist
        '''
        return self._index
    
    @abstractmethod
    def __str__(self):
        '''
        The base string method for all objects in a mesh
        '''
        return f'Mesh object with index {self.index}'

class Point(Mesh_object):
    def __init__(self, index: int, x: float, y: float, z: float):
        '''
        Point class for defining a point in mesh
        '''
        super().__init__(index)
        
        self._x = x
        self._y = y
        self._z = z
    
    @property
    def x(self):
        '''
        Returns the x coordinate of the point
        '''
        return self._x
    
    @property
    def y(self):
        '''
        Returns the y coordinate of the point
        '''
        return self._y
    
    @property
    def z(self):
        '''
        Returns the z coordinate of the point
        '''
        return self._z
    
    def __str__(self):
        '''
        Return a string describing the Point object
        '''
        string = super().__str__()
        string += f'\n  Is Point at (x, y, z): ({self.x}, {self.y}, {self.z})'
        return string
        
class Cell(Mesh_object, ABC):
    def __init__(self, index: int, element_type: int, num_tags: int, physical_entity: int, elementary_entity: int, points: list[int]):
        '''
        Abstract class for defining cells in a mesh.
        
        The object can contain lines, triangles or other poligons
        '''
        super().__init__(index)
        self._type = element_type
        self._num_tags = num_tags
        self._physical_entity = physical_entity
        self._elementary_entity = elementary_entity
        self._points = points
        self._neigbors = []
        self._is_edge = False
    
    @property
    def type(self):
        '''
        Returns the type of cell
        
        1 = line
        2 = triange
        ...
        '''
        return self._type
    
    @property
    def num_tags(self):
        '''
        Returns the number of tags
        '''
        return self._num_tags
    
    @property
    def physical_entity(self):
        '''
        Returns the physical entity
        '''
        return self._physical_entity
    
    @property
    def elementary_entity(self):
        '''
        Returns the elementary entity
        '''
        return self._elementary_entity
    
    @property
    def points(self):
        '''
        Returns the index of the points  
        '''
        return self._points
    
    @property
    def neighbors(self):
        return self._neigbors
    
    @neighbors.setter
    def neighbors(self, neighbors):
        self._neigbors = neighbors
        
    @property
    def is_edge(self):
        return self._is_edge
        
    @abstractmethod
    def __str__(self):
        string = super().__str__()
        string += f'\n  Has element type {self.type}, number of tags is {self.num_tags}, physical entity is {self.physical_entity} and elementary entity is {self.elementary_entity}.'
        string += f'\n  The cell has naboring cells with index of {self.neighbors}.'
        if self.is_edge:
            string += '\n  The cell is a part of the edge.'
        return string

class Triangle(Cell):
    def __init__(self, index, element_type: int, num_tags: int, physical_entity: int, elementary_entity: int, points : list[int]):
        super().__init__(index, element_type, num_tags, physical_entity, elementary_entity, points)
    
    def __str__(self):
        string = super().__str__()
        string += f'\n  The cell is constructed from Points: ({self._points[0]}, {self._points[1]}, {self._points[2]})'
        return string

class Line(Cell):
    def __init__(self, index, element_type: int, num_tags: int, physical_entity: int, elementary_entity: int, points : list[int]):
        super().__init__(index, element_type, num_tags, physical_entity, elementary_entity, points)
    
    def __str__(self):
        string = super().__str__()
        string += f'\n  The cell is constructed from Points: ({self._points[0]}, {self._points[1]})'
        return string

class MeshFactory:
    def __init__(self):
        self._shape = {7: Line, 8: Triangle}
    def register(self, key, shape_class):
        self._shape[key] = shape_class
    def __call__(self, list):
        length = len(list)
        if length not in self._shape:
            return f"error"
        else:
            list = [int(i) for i in list]
            return self._shape[length](list[0], list[1], list[2], list[3], list[4], list[5:])


# class Mesh:
#     def __init__(self, path: Optional[str] = None):
#         '''
#         Creates a class containing lists of points and cells.
#         The class has a read function that reads from .msh file if path exists
        
#         Args:
#             path (str): The path to the .msh file containing the mesh
            
#         Examples:
#             >>> Mesh(my/path.msh)
#             object containing lists based on my/path.msh
#             >>> Mesh()
#             Emptey object
#         '''
#         self._points = []
#         self._cells = []
#         if path:
#             self.mesh = self.read(path)
        
#     def read(self, path: str) -> object:
#         '''
#         Reads from file at path. Saves file content as lists.
        
#         Args:
#             path (str): The path to the .msh file containing the mesh
            
#         Examples:
#             >>> read(my/path.msh)
#             Saves file content as lists at points and cells
#         '''
#         self._physical_names = []
#         with open(path, 'r') as file:
#             while True:
#                 line = file.readline().strip()
#                 if line == '':
#                     break
#                 elif line == '$MeshFormat':
#                     line = file.readline().strip().split(' ')
#                     while line != '$EndMeshFormat':
#                         line = [float(line[0]), int(line[1]), int(line[2])]
#                         self._format = line
#                         line = file.readline().strip()
#                 elif line == '$PhysicalNames':
#                     self._num_physical_names = file.readline().strip()
#                     line = file.readline().strip()
#                     while line != '$EndPhysicalNames':
#                         line = line.split(' ')
#                         line = [int(line[0]), int(line[1]), line[2].strip('"')]
#                         self._physical_names.append(line)
#                         line = file.readline().strip()
#                 elif line == '$Nodes':
#                     line = file.readline().strip()
#                     self._num_nodes = int(line)
#                     line = file.readline().strip().split(' ')
#                     while line[0] != '$EndNodes':
#                         self._points.append(Point(int(line[0]), x=float(line[1]), y=float(line[2]), z=float(line[3])))
#                         line = file.readline().strip().split(' ')
#                 elif line == '$Elements':
#                     line = file.readline().strip()
#                     self._num_elements = line
#                     line = file.readline().strip().split(' ')
#                     while len(line) < 8:
#                         self._cells.append(Line(int(line[0]), element_type=int(line[1]), num_tags=int(line[2]), physical_entity=int(line[3]), elementary_entity=int(line[4]), point_1=int(line[5]), point_2=int(line[6])))
#                         line = file.readline().strip().split(' ')
#                     while line[0] != '$EndElements':
#                         self._cells.append(Triangle(int(line[0]), element_type=int(line[1]), num_tags=int(line[2]), physical_entity=int(line[3]), elementary_entity=int(line[4]), point_1=int(line[5]), point_2=int(line[6]), point_3=int(line[7])))
#                         line = file.readline().strip().split(' ')
                
    
#     @property
#     def points(self):
#         return self._points
    
#     @property
#     def cells(self):
#         return self._cells
    
#     def __str__(self):
#         return f'Mesh with {len(self.points)} points and {len(self.cells)} cells'

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
        self._physical_names = []
        with open(path, 'r') as file:
            factory = MeshFactory()
            while True:
                line = file.readline().strip()
                if line == '':
                    break
                elif line == '$MeshFormat':
                    line = file.readline().strip().split(' ')
                    while line != '$EndMeshFormat':
                        line = [float(line[0]), int(line[1]), int(line[2])]
                        self._format = line
                        line = file.readline().strip()
                elif line == '$PhysicalNames':
                    self._num_physical_names = file.readline().strip()
                    line = file.readline().strip()
                    while line != '$EndPhysicalNames':
                        line = line.split(' ')
                        line = [int(line[0]), int(line[1]), line[2].strip('"')]
                        self._physical_names.append(line)
                        line = file.readline().strip()
                elif line == '$Nodes':
                    line = file.readline().strip()
                    self._num_nodes = int(line)
                    line = file.readline().strip().split(' ')
                    while line[0] != '$EndNodes':
                        self._points.append(Point(int(line[0]), x=float(line[1]), y=float(line[2]), z=float(line[3])))
                        line = file.readline().strip().split(' ')
                elif line == '$Elements':
                    line = file.readline().strip()
                    self._num_elements = line
                    line = file.readline().strip().split(' ')
                    while line[0] != '$EndElements':
                        self._cells.append(factory(line))
                        line = file.readline().strip().split(' ')
    @property
    def points(self):
        return self._points
    
    @property
    def cells(self):
        return self._cells
    
    def __str__(self):
        return f'Mesh with {len(self.points)} points and {len(self.cells)} cells'


def main():
    path = Path.cwd() / Path('simple.msh')
    mesh = Mesh(path)

    for point in mesh.points:
        print(point)
    print()

    for cell in mesh.cells:
        print(cell)
    
if __name__ == '__main__':
    main()