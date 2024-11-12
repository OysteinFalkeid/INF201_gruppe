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

#-------------------------------------------------------------------------------------------------------------------
# Task 2

msh_name = Path.cwd() / Path('simple.msh')
msh = meshio.read(msh_name)
points = msh.points  # mesh points
cells = msh.cells    # mesh cells
cell = cells[1].data[222]
print(cell)
print(cells[1].type)




