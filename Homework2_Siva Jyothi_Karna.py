# Question 1
# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: Consider use range(#begin, #end) method

for i in range(2000,3201):

    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")


## Output: 2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,
# 2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,
# 2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,
# 2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199,


# Question 2
# Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. 
# Suppose the following input is supplied to the program:8
# Then, the output should be:
# 40320

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

def factorial(num):
    a = 1
    for x in range(1, num+1):
        a = a * x
    return a

num = int(input("Type a number: "))
print(factorial(num))

# Output: Type a number: 8
# 40320


# Question 3
# Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()

integral_number = int(input("Type a number: "))

Dictionary = {}
for c in range(1, integral_number+1):
    Dictionary[c] = c*c

print(Dictionary)

# Output: Type a number: 8
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}



# Question 4
# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. 
# Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] 
# ('34', '67', '55', '33', '12', '98')

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple

sequence_numbers = input("Type in numbers seperated only by a comma :")
numbers_split = sequence_numbers.split(',')

numbers_tuple = tuple(numbers_split)

print(numbers_tuple)
print(numbers_split)

# Output: Type in numbers seperated only by a comma :34,67,55,33,12,98
# ('34', '67', '55', '33', '12', '98')
# ['34', '67', '55', '33', '12', '98']

# Question 5
# Question: Define a class which has at least two methods: getString: to get a string from console input printString: 
# to print the string in upper case. Also please include simple test function to test the class methods.

# Hints: Use init method to construct some parameters

class Methods():
    def __init__(self):
        self.str1 = ""

    def getString(self):
        self.str1 = input("Enter String: ")

    def printString(self):
        print(self.str1.upper())

str1 = Methods()
str1.getString()
str1.printString()

# Output: Enter String: jyothi
# JYOTHI

# Question 6
# Question: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example: Let us assume the following comma separated input sequence is given to the program: 100,150,180
# The output of the program should be: 18,22,24

# Hints: If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input.

import math

#Fixed values given
C=50
H=30

Variable = input("Provide D: ")
Variable = Variable.split(',')

Sequence_list = []
for D in Variable:
    Q = round(math.sqrt(2 * C * int(D) / H))
    Sequence_list.append(Q)

print(Sequence_list)

# Output: Provide D: 100,150,180,200,240
[18, 22, 24, 26, 28]


# Question 7
# Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,.., Y-1.
# Example: Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

Input = input("Enter values for X and Y: ")
X_row, Y_col = Input.split(",")
X_row = int(X_row)
Y_col = int(Y_col)

Array = []
for X in range(X_row):
    Matrix = []
    for Y in range(Y_col):
        Matrix.append(X * Y)
    Array.append(Matrix)
    print(Matrix)

print()
print(Array)

# Output: Enter values for X and Y: 5,6
[0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 4, 5]
[0, 2, 4, 6, 8, 10]
[0, 3, 6, 9, 12, 15]
[0, 4, 8, 12, 16, 20]

[[0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5], [0, 2, 4, 6, 8, 10], [0, 3, 6, 9, 12, 15], [0, 4, 8, 12, 16, 20]]


# Question 8
# Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

y=input("Enter comma separated sequence of words : ")
y=sorted(y.split(","))
print(",".join(y))

# Output: Enter comma separated sequence of words : ocean,water,beach,airport,nature,view,land
# airport,beach,land,nature,ocean,view,water


# Question 9
# Question: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be: HELLO WORLD
# PRACTICE MAKES PERFECT

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

Sequence_lines = []
while True:
    sentence = input("Enter Sequence of Lines: ")
    if sentence:
        Sequence_lines.append(sentence.upper())
    else:
        break;
for sentence in Sequence_lines:
    print(sentence)

# Output: Enter Sequence of Lines: enthusiastic automotive engineer
# Enter Sequence of Lines: hello world
# Enter Sequence of Lines: clemson university:
# Enter Sequence of Lines: 
# ENTHUSIASTIC AUTOMOTIVE ENGINEER
# HELLO WORLD
# CLEMSON UNIVERSITY:


# Question 10
# Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.


whitespace_words = "Niagarafalls is beautiful and Atlantic_sea is also beautiful"
seq = whitespace_words.split()
Alphabetical_seq = []
for words in seq:
 
    # If condition is used to store unique string
    # in another list 'Alphabetical_seq'
    if (whitespace_words.count(words)>=1 and (words not in Alphabetical_seq)):
        Alphabetical_seq.append(words)
print(' '.join(Alphabetical_seq))

# Output: Niagarafalls is beautiful and Atlantic_sea also


# Question 25
# Question: Define a class, which have a class parameter and have a same instance parameter.

# Hints: Define a instance parameter, need add it in init method
# You can init a object with construct parameter or set the value later

class Water:
    # Define the class parameter "name"
    name = "Water"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

Ocean = Water("Ocean")
print("%s name is %s" % (Water.name, Ocean.name))

Sea = Water()
Sea.name = "Sea"
print("%s name is %s" % (Water.name, Sea.name))

# Output: # Water name is Ocean
# Water name is Sea


# Question 35
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
# The function should just print the values only.

# Hints: Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

def printDict():
	keys=dict()
	for i in range(1,21):
		keys[i]=i**2
	for (key,value) in keys.items():	
		print(value)

printDict()

# Output: 
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# 121
# 144
# 169
# 196
# 225
# 256
# 289
# 324
# 361
# 400


# Question 36
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
# The function should just print the keys only.

# Hints: Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

def printDict():
	D=dict()
	for i in range(1,21):
		D[i]=i**2
	for key in D.keys():	
		print(key)

printDict()

# Output: 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20


# Question 37
# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# Hints: Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.

def printList():
	lists=list()
	for i in range(1,21):
		lists.append(i**2)
	print(lists)
printList()

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]


# Question 43
# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints: Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.

tuple_list = (1,2,3,4,5,6,7,8,9,10)
new_tuple_list = tuple(num for num in tuple_list if num%2 == 0)
print(new_tuple_list)

# Output: (2, 4, 6, 8, 10)


# Question 51
# Define a class named American and its subclass NewYorker.

# Hints: Use class Subclass(ParentClass) to define a subclass.

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)

# Output: 
# <__main__.American object at 0x7fe724ab09a0>
# <__main__.NewYorker object at 0x7fe724ab0910>


# Question 53
# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

# Hints: Use def methodName(self) to define a method.

class Rectangle(object):
    def __init__(self, len, wid):
        self.length = len
        self.width  = wid

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(10,30)
print(aRectangle.area())

# Output: 300


# Question 54
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# Hints: To override a method in super class, we can define a method with the same name in the super class.

class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.len = length
    def area(self):
        return self.len*self.len

aSquare= Square(5)
print(aSquare.area())

# Output: 25


# Question 56
# Write a function to compute 5/0 and use try/except to catch the exceptions.

# Hints: Use try/except to catch exceptions.


def function():
    return 5/0

try:
    function()
except ZeroDivisionError:
    print("division by zero!")
except Exception:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')


# Output: division by zero!
# In finally block for cleanup



# Question 94
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

# Hints: Use set() to store a number of values without duplicate.

def removeDuplicate( org_list ):
    new_list=[]
    seen = set()
    for item in org_list:
        if item not in seen:
            seen.add( item )
            new_list.append(item)

    return new_list

org_list=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(org_list))


# Output: [12, 24, 35, 88, 120, 155]