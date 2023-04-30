# This program says hello and asks for my name and age and tells me how old I will be in a year.

print('Hello, world!')
print('What is you name?') # ask for name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is you age?') # ask for age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')
