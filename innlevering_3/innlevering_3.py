# Task 1: Regex (3 points)
# Assume that we have sentences of the form

# Ali and Per are friends.
# Kari and Joe know each other.
# James has known Peter since school days.
# The common structure here is that each sentence contains two names and that the names are the only words beginning with capital letters. Create a regular expression that

# matches these sentences (one sentence at a time)
# collects the names in groups
# and write a program that can go through a list of such sentences and print a table of the form (and formatting)

#       Friendships      
# -----------------------
#        Ali - Per       
#       Kari - Joe       
#      James - Peter     
# Assume that

# each sentence begins with a name
# all names only contain letters from A–Z and a–z
# that all names have at least two letters.

# Make sure the program is efficient by ensuring that the regex is not re-parsed
# and compiled each time it is used. Your program should work for all sentences
# with two names that fulfill the previously mentioned rules.

import re

print('Task 1: Regex (3 points)')

sentences = ['Ali and Per are friends.', 'Kari and Joe know each other.', 'James has known Peter since school days.']
names = []

for sentence in sentences:
    names.append(re.findall(r'[A-Z]\w*', sentence))
    
table_width = 31
table =['{:^{width}}'.format('Friendships', width = table_width)]
table.append('{:-^{width}}'.format('', width = table_width))

for name in names:
    table.append('{:^{width}}'.format(name[0] + ' - ' + name[1], width = table_width))

for data in table:
    print(data)

print()
print()
# -------------------------------------------------------------------------------------------------
# Task 2: Password Validation (2 points)
# Write a Python function validate_password that checks if a given password string is valid based on the following rules:

# Starts with an uppercase letter from I to Z.
# Contains at least one word character (a-z, A-Z, 0-9, or underscore).
# Has exactly 4 to 5 characters in length.
# Ends with a digit.
# May contain spaces between the characters but cannot start or end with a space.
# The password must end at the string's end.
# Example passwords:

# Valid: J1234, I_ab5, Z9_w4
# Invalid: A1234 (starts with wrong letter), J12345 (too many characters), I__ (does not end with a digit)

print('Task 2: Password Validation (2 points)')
print()

for i in range(6):

    print('Write a \"strong\" password: ', end='')
    password = input()
    print()

    if re.search(r'^[I-Z]\w{2,3}\d$', password):
        print('OK')
        
    else:
        print('not valid')