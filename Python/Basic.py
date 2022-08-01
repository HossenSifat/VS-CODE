name = 'Tony Stark'
age = 51
print(name)
print(age)
is_tony = True
if is_tony is True:
    print('Tony is a genious')
#s_name = input('what is your superhero name? ')
#print('hello ', s_name)

name = 'Tony Stark'
print(name.upper())
print(name.find('s'))
print(name.find('S'))
print(name.find('Stark'))
print('r' in name)
print(name.replace('Tony Stark', 'Ironman'))
print(name.replace('Stark', 'Ironman'))
print(5//2)
print(5%2) # % is represent reminder
i = 5
# this two method is same
#i = i + 3
i += 3
print(i)
print('nice')
# calculator project
#first_number = input('enter first number: ')
#operator = input('enter operator (+, -, *, /, % ) :')
#second_number = input('enter second number : ')
# first_number = int(first_number)
# second_number = int(second_number)
#
# if operator == '+':
#     print(first_number + second_number)
# elif operator == '_':
#     print(first_number - second_number)
# elif operator == '/':
#     print(first_number / second_number)
# elif operator == '*':
#     print(first_number * second_number)
# elif operator == '%':
#     print(first_number % second_number)
# else:
#     print('invalid number')
# loop
i = 5
while i <= 10:
    print(i)
    i += 1
i = 5
while i <= 10:
    i += 1
    print(i)
i = 1
while i <= 5:
    print(i * '*')
    i = i +1
marks = [97, 85, 98]
print(len(marks))
i =0
while i < len(marks):
    print(marks)
    i +=1
i =0
while i < len(marks):
    print(marks[i])
    i +=1

numbers7 = 4
for count in range(1, 11):
    product = numbers7 * count
    print(numbers7, '*', count, '=', product)

# This is a sample Python script.
print(' hello python world! ')
number = 10
print(number)
website = "mainlycoding.com"
print(website)

# assigning a new variable to website
website = "google.com"
print(website)

#constant
# import constant
# print(constant.PI)
# print(constant.Gravity)

#Number
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#python data convert
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#list
shoppingList = ["apple", "banana", "mango"]
print(shoppingList)
print("first item = ", shoppingList[0])
print("last item = ", shoppingList[2])

#Range of index
shoppingList = ["apple", "banana", "mango", "orange", "pen", "melon", "book"]
print(shoppingList[2:5])
shoppingList[1] = "book"
print(shoppingList)

#python set
demoSet = {"apple", "banana", "mango"}
print(demoSet)

#python tuple
sampleTuple = ("apple", "banana", "mango")
print(sampleTuple)
print(sampleTuple[2])

#python string
sample1 = "This is a string"
print(sample1)
sample2 = '''Here is a multiline
string'''
print(sample2)


#python dictionary
d = {'apple':2,'mango':4}
print(d)
x = d["apple"]
print(x)

# Python Arithmatic Operator
x= 21
y= 7
print("x+y=", x+y)
print("x-y=", x-y)
print("x*y=", x*y)
print("x/y=", x/y)
print("x**y=", x**y)

# Python comparision operator
print("x>y is ", x > y)
print("x<y is ", x < y)
print("x==y is ", x == y)
print("x!=y is ", x != y) #sign mean not equal to
print("x>=y is ", x >= y)
print("x<=y is ", x <= y)

# Python Logical Operator
x= True
y= False
print("x and y is " , x and y)
print("x or y is " , x or y)
print("not y is " , not y)

#python assignment operator
a = 21
b = 10
c = 0
c = a + b
print('Line 1 - value of c is' , c)
c+= a
print('Line 2 - value of c is' , c)
c*=a
print('Line 3 - value of c is' , c)
c/=a
print('Line 4 - value of c is' , c)
c=2
c%=a
print('Line 5 - value of c is' , c)
c**=a
print('Line 6 - value of c is' , c)
c//=a
print('Line 7 - value of c is' , c)

#python if....else statement
num = 2
if num > 0:
    print(num,"is a positive number")
    print('another line of statement')
print('last line of program')

num = -5
if num > 0:
   print("Positive number")
else:
   print("-5 is not a positive number")

num = 0
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

#python for...else loop
numbers = [23, 1, 12, 18, 21, 10, 28, 98, 22]

sum = 0

for val in numbers:
	sum = sum+val

print("The sum is", sum)

digits = [3, 2, 8, 9]

for i in digits:
    print(i)
else:
    print("No items left.")

#python while loop
n = 20

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

#python break statement
# Use of break statement inside the loop

for val in "Bangla":
    if val == "l":
        break
    print(val)

print("The end")

#python continoue statement
for val in "Bangla":
    if val == "g":
        continue
    print(val)

print("The end")

#python function
def add(a,b):
    return (a+b)
print (add(4,7))

#python class
# The blueprint to create cars
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

# Creating some car object
car1 = Car("Red", "bmw")
car2 = Car("White", "toyota")
car3 = Car("Blue", "audi")

# Check whether those cars got different existence in memory or not

print('This car\'s color is ' + str(car1.color) + ' and brand name is ' + car1.brand)
print('This car\'s color is ' + str(car2.color) + ' and brand name is ' + car2.brand)
print('This car\'s color is ' + str(car3.color) + ' and brand name is ' + car3.brand)

# import name
# print(name.my_name)

# sentence = 'my dog name is sammy'
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.capitalize())
# print(sentence.count('m'))

#string code
first_name= 'sifat'
last_name = 'hossen'
#first_name = input('please enter your first name')
#last_name = input('please enter your last name')
#print('Hello' + first_name +" " + last_name )
print('Hello ' + first_name.capitalize() +" " + last_name.capitalize() )
print('Hello, {} {}'.format(first_name, last_name))
print('hello, {1} {0}'.format(first_name.capitalize(), last_name.capitalize()))
print('hello, {} {}'.format(first_name, last_name))
print(f'hello, {first_name} {last_name}')

#string addition
days_in_feb = 28
print(str(days_in_feb) + ' days in feb')
first_num = '5'
second_num = '6'
print(first_num + second_num)
print(int(first_num)+ int(second_num))
print(float(first_num)+ float(second_num))

#dates
import datetime
import math
from tracemalloc import start
import turtle
current_date = datetime.datetime.now()
print('today is: ' + str(current_date))
#one_day = datetime(days=1)
#yesterday = current_date - one_day
#print('yesterday was:' + str(yesterday))
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))
#birthday= input('When is your birthday? ')
#birthday_date = datetime.datetime.strptime(birthday, '%d/%m/%y')
#print('birthday: ' + str(birthday_date))

def greet(name):
    print('hello', name)
    print('how are you')
greet('jack')

def add(a,b):
    return (a+b)
print(add(4,7))

def add_numbers(n1, n2, n3):
    result= n1 + n2 + n3
    print('the sum is ', result)
number1 = 3
number2 = 5 
number3 = 4
add_numbers(number1, number2, number3)

# find grade & average mark
marks = [55,66,87,94,76]
length = len(marks)
print('length is', length)

# marks_sum = sum(marks)
# print('The total marks you got is', marks_sum)

def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subject = len(marks)
    average_marks = sum_of_marks / total_subject
    return average_marks

def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade =  'B'
    elif average_marks >= 40:
        grade = 'C'
    else:
        'failed'
    return grade

# marks = [56,85,87,72,92]
# find_average_marks(marks)
# average_marks =find_average_marks(marks)
# print('your average marks is:', average_marks )

# grade = compute_grade(average_marks)
# print('your grade is:', grade)

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))
num = 5
print('The factorial of', num, 'is', factorial(num))

def double(x):
    return x*2
x = 6
print(double(x))

double = lambda n:n*3
print(double(2))

larger = lambda a,b:a if a>b else b
print(larger(45,55))

names = ['asif', 'niloy', 'shuvo', 'sifo', 'zlatan']
names.sort(key=lambda x: len(x))
print(names)

number= [1, 5, 8 ,7 ,9 ,6 ]

square_nums = []
square = lambda n : n**2
for num in number:
    square_nums.append(square(num))
print(square_nums)

square_nums = list(map(lambda n: n**2, number))
print(square_nums)

even_numbers = list(filter(lambda n: n%2 == 0, number))
print(even_numbers)

#swap two variable
a = 5
b = 6

# temp = a
# a= b
# b = temp

# a = a + b #11
# b = a-b # 5
# a = a - b #6

# a = a ^ b # XOR method
# b = a ^ b
# a = a ^ b

a,b = b,a #right side assign first

print(a)
print(b)

#converting celsius to fahrenheit

celsius = 22
fahrenheit = (celsius * 1.8) +32
print(fahrenheit)
print('%.2f celsius = %.2f fahrenheit' %(celsius, fahrenheit))

#prime number
num = 7

for i in range(2,num):
    if num % i == 0:
        print('Not prime number')
        break
else:
    print('prime number')

#even number
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
even_numbers = []

starting = 0
# while starting < 100:
#     if is_even(starting):
#         print(f'{starting} is Even')
#     else:
#         print(f"{starting} is Odd")
#     starting = starting + 1
# while starting < 100:
#     if is_even(starting):
#         even_numbers.append(starting)
#     starting = starting + 1

for value in range(0, 50):
    if is_even(value):
        even_numbers.append(value)

#print(even_numbers)
print(f"Even number:{even_numbers}")
print("Finished")


with open("pytext.txt", mode="r") as r_qoute:
    words_all = []
    for line in r_qoute.readlines():
        words = line.strip().split(" ")
        words_all += words
    unique_words = set(words_all)
    print(words_all)
    print(len(unique_words))

    with open("unique_words.txt", mode = "w") as u_word:
        for item in sorted(unique_words):
            u_word.write(item)
            u_word.write("\n")



print("finished")




