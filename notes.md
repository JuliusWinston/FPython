# BEGINNER PYTHON LESSONS

## A program that asks the user for his/her password and gives or denies access based on the password

    password = "opensesame"
    print("Enter password to continue: ")   Do something
    typePass = input()
    if typePass == password:
        print("Access Granted, You may go ahead now!")
    else:
        print("You do not have access to this section, please leave!")

    for i in range(20): Do this action exactly 20 times
        print("Hello World!")

    i = 0
    while i < 20:
        print("Hello world!")
        i=i+1

## Asking Smart Programming Questions

1. Explain what you are trying to do, not just what you did.
2. Specify line at which point the error occurs.
3. Copy and paste the entire error message and your code to the platform links you want to post.
4. Explain what you've already tried to do to fix the program.
5. List the version of python you're using.
6. If error occurs after a particular change, add it.
7. Say whether you're able to reproduce the error every time you run the program.

[Github](https://github.com/JuliusWinston/FPython/blob/master/basic.py)

## Data Types

A category for values, and every value belongs to one data type.
Integers: -2, -1, 0, 1, 2, 3, 4
Floating-point numbers (float): -1.25, -1.0, -0.5, 0.0, 1.0, 1.25
String (str): 'a', 'aa', 'aaa', 'Hello!', '11', '12 cats'

    def double (first):
        doubleTotal = first * 2
        print("Doubling the number gives: " + str(doubleTotal))

    double(4)

## Semantic / Logical error

* 'Hello world'
* 'Welcome to python 101'
* 'Programming is fun!'
* "Happy coding!"

## Operands / Data type

### Operators:
* Exponent                                  **          2**3       8
* Modulus/remainder                          %          22 % 8     6
* Integer division / floored quotient       //          22 // 8    2
* Division                                   /          22 / 8     2.75
* Multiplication                             *          3 * 5      15
* Subtraction                                -          5 - 2      3
* Addition                                   +          2 + 2      4

Operator Precedence / Order of operation
**, *,/,//,%, +, -
1st,    2nd    3rd

2 + 3 * 6 = 20
(2 + 3) * 6
(2 + 3) * 6 - (2 - 6)
48565878 * 578453
2 ** 8
23 / 7
23 // 7
23 % 7
2        +        2
2+2
(5 - 1) * ((7 + 1) / (3 - 1))
    4   * (8 / 2)
    4   *    4
    16

String concatenation
'Alice' + 'Kofi' + "34"

String replication
'Kofi' * 5

Variable

spam = 34
spam

Assignment Operator (=)
variable = value (e.g eggs = 56)

Equality Operator (==)
value == value (e.g eggs == spam)

Variable Names
Rules to follow when naming variables in python:
1. It can only be one word with no spaces
2. It can only use letters, numbers, and the underscore(_) character
3. It can't begin with a number

Valid variable names (examples):
current_balance
currentBalance
account4
_42
TOTAL_SUM
hello

Invalid variable names (examples):
current-balance
current balance
42
TOTAL_$UM
'hello'

NB: In python, variable names are case-sensitive
spam, SPAM, Spam, SPam

Variable naming conventions
Aside: camel case, Pascal case, Snake case

currentCustomerBalance - camel casing
CurrentCustomerBalance - pascal casing
current_customer_balance - snake casing (python likes this)
CURRENT_CUSTOMER_BALANCE - snake casing

## Disecting our first program

* Line 1 - Any line following '#' is a comment and is ignored by python.
* Line 2 - Blank lines are also ignored by python.
* Line 3 - The print() function displays the string value inside its parentheses on the screen.
* Line 5 - The input() function waits for the user to type some text on the keyboard and press ENTER.
* Line 8 - The len() function takes a string value and gives you an integer value for the number of characters in that string.

## The str(), int(), and float() Functions

str(int) converts an numbers to string  
int(value) convers valid figure values into integers
float('4.90')
float(5)