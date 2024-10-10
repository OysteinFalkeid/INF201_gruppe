
#Task 0 —Warm up exercise (0 points)
#First try
#due to a missunderstanding this solution is wrong
print('Task 0 —Warm up exercise (0 points)')

import random

players = {'Sarah': {'points': 0},'Titus': {'points': 0},'Hanna': {'points': 0}}
rounds = 4

#this function dose not work as intended in the Task description
def rol(name: str, Players: dict) -> None: 
    Players[name]['points'] += random.randint(1,6)

for i in range(rounds):
    rol('Sarah', players)
    rol('Titus', players)
    rol('Hanna', players)


print(players)


#---------------------------------------------------------------------------------------------
#As I have nott gotten .ipynb files to work with .venv I am using a delere all variables loop
#This delets all variables not starting with a '_'
import sys
system = sys.modules[__name__]
for name in dir():
    if name[0]!='_' and not name == 'system': delattr(system, name)

#---------------------------------------------------------------------------------------------
#Task 0—Warm up exercise (0 points)
print()
print('#Task 0—Warm up exercise (0 points)')

import random

players = {}
game_results = {}
rounds = 4

inputs = False
i = 0

while not inputs:
    print(players)
    print('add players or write stop: ', end='')
    new_player = input()
    if new_player == 'stop':
        inputs = True
    else:
        players.update({'player' + str(i) : new_player})
        i += 1
print(players)
print(players['player1'])


def rol(name: str, Game_Results: dict) -> None:
    try:
        Game_Results.update({name: {'points': Game_Results[name]['points'] + random.randint(1,6)}})
    except KeyError:
        Game_Results.update({name: {'points': random.randint(1,6)}})
         
for i in range(rounds):
    for player in range(len(players)):
        rol(players['player' + str(player)], game_results)

print(game_results)

#---------------------------------------------------------------------------------------------
#As I have nott gotten .ipynb files to work with .venv I am using a delere all variables loop
#This delets all variables not starting with a '_'
import sys
system = sys.modules[__name__]
for name in dir():
    if name[0]!='_' and not name == 'system': delattr(system, name)

#---------------------------------------------------------------------------------------------
#Task 1—Counting votes (3 points)
print()
print('Task 1—Counting votes (3 points)')

from typing import Optional

with open("2021-09-14_party distribution_1_st_2021.csv", "r", encoding="utf-8") as csv_file:
    headders = csv_file.readline().replace("\n","").split(";")[:-1]
    data = [line.strip().split(";")[:-1] for line in csv_file.readlines()]

print('Task 1 part 1')
index_fylkenavn = headders.index('Fylkenavn')
index_partikode = headders.index('Partikode')
index_antall_stemmer_totalt = headders.index('Antall stemmer totalt')

print(index_fylkenavn, index_partikode, index_antall_stemmer_totalt)

table_headders = [headders[index_partikode], headders[index_antall_stemmer_totalt]]
table_data = []

for line in data:
    if line[index_partikode] not in [sublist[0] for sublist in table_data]:
        table_data.append([line[index_partikode], 0])
    table_data[[sublist[0] for sublist in table_data].index(line[index_partikode])][1] += int(line[index_antall_stemmer_totalt])

table_data.sort(key=lambda x: x[1], reverse=True)
    
def print_table(Table_Data: list = [], Headder: Optional[list] = [], coloumn_width: Optional[int] = None) -> None:
    if coloumn_width:
        pass
    else:
        coloumn_width = len(
            max([max(Headder, key=len), 
            max([sublist[0] for sublist in Table_Data], key=len), 
            str(max([sublist[1] for sublist in Table_Data]))], key=len)) + 2
        
    if Headder:
        print_line_of_stars(coloumn_width*len(Headder)+len(Headder)+1)
        print('*', end='')
        for headder in Headder:
            print('{data: >{width}}'.format(data = headder, width = coloumn_width), end='')
            print('*', end='')
        print()
        print_line_of_stars(coloumn_width*len(Headder)+len(Headder)+1)
    for line in Table_Data:
        for Data in line:
            print('*', end='')
            print('{data: >{width}}'.format(data = Data, width = coloumn_width), end='')
        print('*')
    print_line_of_stars(coloumn_width*len(Headder)+len(Headder)+1)
    
def print_line_of_stars(length: int = 0) -> None:
    print('{data:*<{width}}'.format(data = '', width = length))

print('Task 1 part 2')
print_table(table_data, Headder=table_headders)

table_headders.append('Prosent')
total_vote_count = 0

for line in table_data:
    total_vote_count += line[1]
for line in table_data:
    line.append(round(float(line[1])/total_vote_count*100, ndigits=2))

print('Task 1 part 3')
print_table(table_data, Headder=table_headders)

table_headders.append('Mer en 4% av stemmene')

for i, line in enumerate(table_data):
    if line[2] > 4:
        line.append(1)
    else:
        line.append(0)

print('Task 1 part 4')
print_table(table_data, Headder=table_headders)

def count_votes_from_file(path: str = '', line_number: Optional[int] = 0) -> None:
    
    with open(path, "r", encoding="utf-8") as csv_file:
        headders = csv_file.readline().replace("\n","").split(";")[:-1]
        data = [line.strip().split(";")[:-1] for line in csv_file.readlines()]

    #index_fylkenavn = headders.index('Fylkenavn')
    index_partikode = headders.index('Partikode')
    index_antall_stemmer_totalt = headders.index('Antall stemmer totalt')
    
    table_headders = [headders[index_partikode], headders[index_antall_stemmer_totalt]]
    table_data = []

    for line in data:
        if line[index_partikode] not in [sublist[0] for sublist in table_data]:
            table_data.append([line[index_partikode], 0])
        table_data[[sublist[0] for sublist in table_data].index(line[index_partikode])][1] += int(line[index_antall_stemmer_totalt])

    table_data.sort(key=lambda x: x[1], reverse=True)
        
    def print_table(Table_Data: list = [], Headder: Optional[list] = [], coloumn_width: Optional[int] = None) -> None:
        if coloumn_width:
            pass
        else:
            coloumn_width = len(
                max([max(Headder, key=len), 
                max([sublist[0] for sublist in Table_Data], key=len), 
                str(max([sublist[1] for sublist in Table_Data]))], key=len)) + 2
            
        if Headder:
            print_line_of_stars(coloumn_width*len(Headder)+len(Headder)+1)
            print('*', end='')
            for headder in Headder:
                print('{data: >{width}}'.format(data = headder, width = coloumn_width), end='')
                print('*', end='')
            print()
            print_line_of_stars(coloumn_width*len(Headder)+len(Headder)+1)
        for line in Table_Data:
            for Data in line:
                print('*', end='')
                print('{data: >{width}}'.format(data = Data, width = coloumn_width), end='')
            print('*')
        print_line_of_stars(coloumn_width*len(Headder)+len(Headder)+1)
        
    def print_line_of_stars(length: int = 0) -> None:
        print('{data:*<{width}}'.format(data = '', width = length))

    table_headders.append('Prosent')
    total_vote_count = 0

    for line in table_data:
        total_vote_count += line[1]
    for line in table_data:
        line.append(round(float(line[1])/total_vote_count*100, ndigits=2))

    table_headders.append('Mer en 4% av stemmene')

    for i, line in enumerate(table_data):
        if line[2] > 4:
            line.append(1)
        else:
            line.append(0)
    
    if line_number:
        for i in range(len(table_data)):
            if i > line_number-1:
                for j in range(len(table_data) - i):
                    table_data.pop(i)
         
    print_table(table_data, Headder=table_headders)

print('Task 1 part 5 first table with 3 lines')
count_votes_from_file("2021-09-14_party distribution_1_st_2021.csv", 3)
print('Task 1 part 5 second table with 7 lines')
count_votes_from_file("2021-09-14_party distribution_1_st_2021.csv", 7)

#---------------------------------------------------------------------------------------------
#As I have nott gotten .ipynb files to work with .venv I am using a delere all variables loop
#This delets all variables not starting with a '_'
import sys
system = sys.modules[__name__]
for name in dir():
    if name[0]!='_' and not name == 'system': delattr(system, name)

#---------------------------------------------------------------------------------------------
#Task 2-ASCII and UTF-8 (2 points)
print()
print('Task 2-ASCII and UTF-8 (2 points)')


def ASCII_to_binary_convert(characters: list) -> None:
    for char in characters:
        print('Character: ' + char)
        if ord(char) < 2**7:
            print('- ASCII representation: ' + format(ord(char), '08b'))
        else:
            print('- Not in ASCII range')



ASCII_to_binary_convert(['2', '$', 'å'])


#---------------------------------------------------------------------------------------------
#As I have nott gotten .ipynb files to work with .venv I am using a delere all variables loop
#This delets all variables not starting with a '_'
import sys
system = sys.modules[__name__]
for name in dir():
    if name[0]!='_' and not name == 'system': delattr(system, name)

#---------------------------------------------------------------------------------------------
#Task 3-ASCII and UTF-8 (2 points)
print()
print('Task 3-ASCII and UTF-8 (2 points)')


def ASCII_to_binary_convert(characters: list) -> None:
    for char in characters:
        print('Character: ' + char)
        if ord(char) < 2**7:
            print('- ASCII representation: ' + format(ord(char), '08b'))
            print('- UTF-8: ' +  format(char.encode('utf-8')[0], '08b') + ' (1 byte)')
        else:
            print('- Not in ASCII range')
            print('- UTF-8: ', end='')
            for i in range(len(char.encode('utf-8'))):
                print(format(char.encode('utf-8')[i], '08b') + ' ', end='')
            print(' (' + str(len(char.encode('utf-8'))) + ' bytes)') 



ASCII_to_binary_convert(['2', '$', 'å', '€' , 'æ', 'Æ'])
