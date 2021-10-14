from math import *
#A comment
"""multi
line
comment"""

print("6 Hello World")

name = "John"
age = "70"
#concatenation
print("12 " + name + " is " + age + " years old")

#escape character
print("14 Hello\nworld")
print("15 Hello\"world")

#string functions
print("18 " + name.lower())
print("19 " + name.upper())
print("20 {}".format(name.isupper())) #format bool to str
print("21 {}".format(len(name)))
print("22 {}".format(name[0]))
print("23 {}".format(name.index("h")))
print("24 {}".format(name.replace("n","nathan")))
print("25 " + str(age))

#num functions
print("28 "+ str(abs(-5)))
print("29 " + str(pow(3, 3)))
print("30 " + str(round(3.2)))
print("31 " + str(floor(3.2)))
print("33 " + str(ceil(3.2)))

#user input
#name = input("Enter your name: ")

#lists
num_list = [11, 22, 33, 44, 55, 66]
print("40 " + str(num_list[1:4]))
num_list.extend(num_list)
print("42 " + str(num_list))
num_list.append(77)
print("44 " + str(num_list))
num_list.insert(1, 12)
print("46 " + str(num_list))
num_list.remove(num_list[1])
print("48 " + str(num_list))
num_list.pop()
print("50 " + str(num_list))
print("51 " + str(num_list.count(11)))
num_list.reverse()
print("53 " + str(num_list))
num_list.sort()
print("55 " + str(num_list))
num_list2 = num_list.copy()
num_list.clear()
print("58 " + str(num_list))
print("59 " + str(num_list2))

#tuples (immutable)
coordinates = (3, 4, 5)
print("63 " + str(coordinates[1]))

#functions
def say_hi(name):
    print("67 Hello " + name)
say_hi("Deivis")

def cube(num):
    return num * num * num
print("72 " + str(cube(3)))

#if else statements with 'and', 'or' and not() logical operators and == !=
if_number = 2
if if_number > 2 and if_number <= 4:
    print("77 More than 2 and less or equals 4")
elif if_number > 4:
    print("79 More than 4")
else:
    print("81 Less than or equals 2")

#Dictionaries
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April"
}
print("90 " + str(month_conversions["Jan"])) #or month_conversions.get("Jan")

#while loop
while_index = 1
while while_index <= 10:
    print("95 While index " + str(while_index))
    while_index += 1

#for loop
for letter in "Word":
    print("100 " + letter)
for index in range(10):
    print("102 " + str(index))

#try except
try:
    try_zero = 10 / 0
    try_input = int(input("107 Enter a number: "))
except ZeroDivisionError as err:
    print("109 " + str(err))
except ValueError:
    print("111 Invalid input")

#Importing a .py file
#import useful_tools
#print(useful_tools.function(parameter))

#classes and objects
#create a separate file Student.py
class Student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major
    def on_honor_roll(self):
        if self.gpa >= 9:
            return True
        else:
            return False
#From Student import Student -> imports Student class
student1 = Student("Dave",10,"CS")
print("131 " + str(student1.name))
print("132 " + str(student1.on_honor_roll()))

#Inheritance
class Grad_Student(Student):
    def __init__(self, name, gpa, major, job):
        self.name = name
        self.gpa = gpa
        self.major = major
        self.job = job
student2 = Grad_Student("John", 8, "CS", "Janitor")
print("142 Student 2 is on honor roll: " + str(student2.on_honor_roll()) + ", occupation: " + str(student2.job))



# Official python tutorial

# _ in interactive mode takes the last output (except for print statements)

# Math operators
print(10 + 2)
print(10 - 2)
print(10 * 2)
print(10 / 2) #returns a float value
print (10 // 4) #floor division
print(10 ** 2) #power

# Python also supports other types of numbers, such as Decimal and Fraction. 
# Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j)


# Strings
print('doesn\'t') # \ is used to escape strings
print("Hello\nWorld") # \n makes new line
print(r"Hello\nWorl\'d") # preface r before string reads line without escape characters
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""") # triple quotes print the string as it is formatted. \ at the end of the line prevents a new line
print(3 * "um" + "ium") # 3 times "um" and appends "ium" at the end
print("Py" "thon") # 2 strings next to each other are concatenated automatically (only works with string literals, not vars)
word = "Python"
print(word[0]) # prints individual letters
print(word[4])
print(word[-1]) # starts from the back
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end
# Sstring slices and indexes are immutable. To change a letter in a string variable you should create a new string variable
print(len(word)) #prints the length of the string


# Lists
numbers = [1, 4, 9, 16, 25]
print(numbers[3])
print(numbers[2:]) # same slicing rules as in string
extended_numbers = numbers + [36, 49, 64, 81, 100] # concatenation is allowed
numbers[2] = 8 # lists are mutable
numbers[2:5] = [2, 3, 4] # lists are mutable in slices also
numbers.append(36) # appends a value to the back of the list
print(len(numbers)) # len function also applies to lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = [list_a, list_b] # nested list
print(list_c[0])
print(list_c[0][0])
num_a, num_b = 0, 1 # multiple assingment


# Control flow statements
# while statement
while num_a < 10:
    print(num_a)
    num_a, num_b = num_b, num_a + num_b

# for statement
for number in list_a:
    print(number)
# to modify a looped list create a copy of that list
list_a_copy = list_a.copy()

# if statement
if num_a < 0:
    num_a = 0
    print('Negative changed to zero')
elif num_a == 0:
    print('Zero')
elif num_a == 1:
    print('Single')
else:
    print('More')

# range function
start = 1
end = 10
step = 2
for i in range(start, end, step):
    print(i)

# break statement and else clause for for loop (When break statement is executed inside a loop, else will not initiate)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# continue statement will execute the next iteration of the loop without finishing the code beneath
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# pass statement will fill pass a statement where it is nescessary to have one, and will run without giving an error
number = 5.5
if number > 0.0:
    pass

# functions and procedures (procedures don't return a value)
# functions are independent, and methods belong to objects
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n.""" # This is a docstring.
    # There are tools which use docstrings to automatically produce online 
    # or printed documentation, or to let the user interactively browse through code; 
    # it’s good practice to include docstrings in code that you write, so make a habit of it
    a, b = 0, 1 # Local variables
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
# Now call the function we just defined:
fib(2000)
print(fib.__doc__) # This prints out the docstring

# Default values in function arguments
# This function can be called with fewer than 3 arguments
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'): # The in keyword tests whether or not a sequence contains a certain value.
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# The default values are evaluated at the point of function definition in the defining scope, so this will print 5:
i = 5
def f(arg=i):
    print(arg)
i = 6
f()

# All these values were positional arguments. You can also use keyword arguments:
f(arg = 5)
# In a function call, keyword arguments must follow positional arguments. 
# All the keyword arguments passed must match one of the arguments accepted by the function.
# No argument may receive a value more than once.

# *name parameter recieves a tuple, **name argument recieves a dictionary. *name must go before **name.
# If you use tuple first and then a normal argument, use keyword parameter to break out of the tuple parameter
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# Parameters before / in a function are position-only, parameters after * are keyword only
def parameter_types(param1, /, *, param3):
    print(param1, param3)
parameter_types("Hello", param3="world")

# Lambda functions are single expression anonymous functions
larger = lambda a,b : a if a>b else b
print(larger(4,5))
# It can also be used to sort arrays in a specific way with 'key' keyword parameter
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1]) # This array of tuples is being sorted by the second member of the tuple pair
print(pairs)

list_a = [1, 2, 3, 4, 5, 6]
list_a.append(7) # Adds a value to the end of the list
list_a.extend([8, 9, 10]) # Adds an iterable to the end of the list
list_a.insert(3, 999) # Inserts 999 into index 3 and pushes the entire remaining list further down
list_a.remove(999) # Removes a value from the list
print(list_a.pop()) # Remove the item at the given position in the list, and return it.
                    # If no index is specified, a.pop() removes and returns the last item in the list.
print(list_a.index(1)) # Returns the index of the value
print(list_a.count(1)) # Returns the count of a given value
list_a.sort() # Sorts the list
list_a.reverse() # Reverse the elements of the list in place
list_a.copy() # Returns a shallow copy of the list

# List comprehensions
vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec]) # x is the iterated member. Expression at the beginning gets printed
print([x for x in vec if x >= 0]) # x gets in the list if it satisfies the condition
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]) # Double for loop
i = 1
print([[i for i in range(i, 10) if i <= j] for j in range(3)]) # Nested list comprehensions
del vec[0] # Deletes indexes in lists or entire variables
print(vec)

# Tuple unpacking
tup = ("Hello", 3, "x")
x, y, z = tup
print(x, y, z) # These variables will all have one value each from the tuple

# A set is an unordered collection with no duplicate elements.
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
a = set('abracadabra') # These will return every reocurring letter only once
b = set('alacazam')
print(a - b) # Letters in a but not in b
print(a | b) # Letters in a or b or both
print(a & b) # Letters in both a and b
print(a ^ b) # Letters in a or b but not both
# Set comprehensions work similar to list comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}

# Dictionaries: indexed by keys, which are immutable types: strings, numbers or tuples
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127 # Adds a new pair to the dictionary
del tel['sape'] # Removes an entry from the dictionary
dict_comp = {x: x**2 for x in (2, 4, 6)} # A dictionary comprehension
tel = dict(sape=4139, guido=4127, jack=4098) # Another way to initiate a dictionary