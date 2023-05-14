# A program that displays a welcome message to Franklin and grants access if the password is 'Swordfish'

# name = 'Franklin'
# password = 'Swordfish'
# if name == 'Franklin':
#     print('Hello, Franklin')
#     if password == 'Swordfish':
#         print('Access Granted')
#     else:
#         print('Wrong Password')

# print('End of program')

# e.g of a while loop

# steps (algorithm)
# assign 0 to variable count
# while count is less than 5 print/display count (the value stored in count) to the screen 
# increase count by 1
# print/display "End of loop" to the screen

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
# print("End of loop")

# number = 0
# while number < 7:
#     print('Hello, world!')
#     number = number + 1
# print('End of loop')

# total = 0
# count = 1

# while count <= 10:
#     total = total + count
#     count = count + 1

# print(total)

print('Please enter password')
password = input()

while password != 'king':
    print('Please enter correct password...')
    password = (input())

print('Welcome to the program')