#prints the question without linebreak
print("Hi what is your name: ", end="")
#gets the user input and stores data in he name variable
name = input()
#prints a new line for some brething room
print()
#converts the name variable inn to a nice greeting
greeting = "* Hello " + name +" nice to meet you *"

#prints the topp border
for i in (greeting):
    print("*", end="")
print()

#prints the greeting
print(greeting)

#prints the bottom border
for i in (greeting):
    print("*", end="")
print()