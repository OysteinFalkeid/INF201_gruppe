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

#-------------------------------------------------------------------------------------------------------------------
# Task 2


class mesh:
    def __init__(self):
        self._point = []
        self._cell = []
        
    def read(self, path: str) -> object:
        msh = meshio.read(path)
        return msh
            

class point:
    def __init__(self, x, y):
        self._x = 0.0
        self._y = 0.0
        

class cell(ABC):
    def __init__(self):
        super().__init__()
        







