# BEGINNER PYTHON LESSONS

## WEEK 1

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

### Operators (Arithmetic)

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

## WEEK 2

## Flow Control

## Boolean Values (True or False)

While the integer, floating-point, and string data types have an unlimited
number of possible values, the Boolean data type has only two values: True
and False.

## Comparison Operators

* Equal to                      ==
* Not equal to                  !=
* Less than                     <
* Greater than                  >
* Less than or equal to         <=
* Greater than or equal to      >=

## Boolean Operators (and, or, not)

- Binary Boolean Operators (and, or) 
- Not operator (not)

### Truth table for and

True and True     True
True and False    False
False and True    False
False and False   False

### Truth table for or

True or True     True
True or False    True
False or True    True
False or False   False

### Truth table for not

not True      False
not False     True

## Mixing Boolean and Comparison Operators

(4 < 5) and (5 < 6)
(4 < 5) and (9 < 6)
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2

The Boolean operators have an order of operations just like the
math operators do. After any math and comparison operators evaluate,
Python evaluates the not operators first, then the and operators, and then
the or operators.

## Blocks of code

### Three rules

* Blocks begin when the indentation increases.
* Blocks can contain other blocks.
* Blocks end when the indentation decreases to zero or to a containing block’s indentation.

## Program Execution

## Flow Control Statements

### if statement

consists of:

* if keyword word (reserved words)
* A condition (that is, an expression that evaluates to True or False)
* A colon
* Starting on the next line, an indented block of code (called the if clause)

### else statement

consists of:

* else keyword
* a colon
* Starting on the next line, an indented block of code (called the else clause)

e.g

    if name == 'Sensei':
        print('Hello, Sensei')
    else:
        print('Hi, Stranger')

### elif statements

* if keyword word (reserved words)
* A condition (that is, an expression that evaluates to True or False)
* A colon
* Starting on the next line, an indented block of code (called the if clause)

e.g

    if name == 'Sensei':
        print('Hello, Sensei')
    elif age < 12:
        print('You are not Sensei, you are a kid')

## While Loop statements

You can make a block of code execute over and over again using a while
statement. The code in a while clause will be executed as long as the while
statement’s condition is True. In code, a while statement always consists of
the following:

* the while keyword
* A condition (that is, an expression that evaluates to True or False)
* A colon
* Starting on the next line, an indented block of code (called the
while clause)

e.g write a program that displays the total/sum of the first 10 numbers starting from 1

solution: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

breakdown of the solution:

step 0: 1 <br >
step 1: 1 + 2 = 3 <br >
step 2: 3 + 4 = 7 <br >
step 3: 7 + 5 = 12<br >
step 4: 12 + 6 = 18<br >
step 5: 18 + 7 = 25<br >
step 6: 25 + 8 = 33<br >
step 7: 33 + 9 = 42<br >
step 8: 42 + 10 = 52

PS: we missed a step which was adding 3

answer = 55