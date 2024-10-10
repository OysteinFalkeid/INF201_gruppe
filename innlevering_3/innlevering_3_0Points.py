# Task 0: Warm-up exercise (0 points)
# Assume a file with the content

# The following document contains several email addresses. They all have the form example.name@institution.domain, example-name@institution.domain, or example_name@institution.domain. 

# Two examples with the nmbu domain are jonas.kusch@nmbu.no or lena.scholzer@nmbu.no.
# Two examples with a generic domain are jonas.kusch@gmail.domain or lena-scholzer@nmbu.domain.
# Write a function that, given a file name, goes through the file (skipping its first line) and finds all email addresses. The program identifies the name, the institution, and the domain. Once you are done, you can compare your program to the one presented in this video.

import re

with open('email_list.txt', 'r',  encoding="utf-8") as email_file:
    headder = email_file.readline()
    data = [line.strip().split(' ') for line in email_file]

email_list = []

for line in data:
    for string in line:
        if re.search('@', string):
            email_list.append({'first name': re.findall(r'\A\w+', string)[0], 'last name': re.findall(r'[\.|\-|\_](\w+)[\@]', string)[0], 'e-mail': string, 'domain': re.findall(r'\.(\w+)', string)[len(re.findall(r'\.(\w+)', string))-1]})
table_width = 28

print()
for key in email_list[0]:
    print('{:^{width}}'.format(key, width = table_width), end='')
print()
for dictionary in email_list:
    for key in dictionary:
        print('{:^{width}}'.format(str(dictionary[key]), width = table_width), end='')
    print()
print()

#--------------------------------------------------------------------------------------------------
# Task 3: Challenge Exercise (0 points)
# Write a program that goes through all the python files in the current working directory and prints out all imports per file. Here, an import means the word that follows the keyword «import». Your program should be able to find patterns beginning with «import» and «from».

# Assume you have a file «dummy.py» with the following lines:
#--------------------------------------------------------
#     import re # this imports re                       -
#     from pathlib import Path # this imports Path      -
#--------------------------------------------------------
# Then, the output of your program should look like:
#--------------------------------------------------------
#     path/to/file/dummy.py: ['re']                     -
#                                                       -
#     path/to/file/dummy.py: ['Path']                   -
#--------------------------------------------------------
# You can assume that module and package names only have word characters and that imports end with a white space. Proceed as follows:

# Use the compile function to construct two regular expressions to find and return the package name in
# lines starting with «import»
# lines starting with «from»
# Use the pathlib-module to find all files in the current working directory which end with «.py».
# Iterate through all the lines of the found files and extract the import names using the compiled regular expressions.
# If the file contains any imports, print the path of the file along with the packages that are imported.
print('Task 3: Challenge Exercise (0 points)')
print()

import re
from pathlib import Path

current_path = Path.cwd()

for py in current_path.glob('*.py'):
    with open(py, 'r', encoding='utf_8') as py_file:
        for line in py_file.readlines():
            for ip in re.findall(r'import\s(\w+)', line):
                print(str(py) + ': [\'' + str(ip) + '\']')