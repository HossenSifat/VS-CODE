var= 'study mart'
print(id(var))
from operator import truediv
import sys
print(sys.getsizeof(var)) 
s, y, e = 10, 54 ,66
print(y)
data = '60 Days of python'
print(data.find('s'))
print(data.find('y', 6))
print(data.swapcase())
print(data.title())
print(data.isdigit())
print(data.split())
print(data.split()[1])
print(data.center(100))
x = range(0, 13,2)
for i in x:
    print(i, end= ',')

x = range(13, 2,-3)
for i in x:
    print(i)  

x = 5 
y = 4
print(x**y)
import math
print(math.ceil(x/y))
a = 10152349455
b = 10152349455
print(id(a))
print(id(b))
print(a == b)
print(a is b)
print(x ^ y)

# length = input('The value of length is: ', )
# breadth = input ('The value of breadth is: ', )
# if length == breadth :
#     print('This is a square')
# else:
#     print('This is not square')

f = 2 
g = 5
c = 3
print(max(f, g, c))

# attendance = int(input('The attendance of sifat is : ', ))
# if attendance < 75 :
#     print('The student will not be allowed to sit in exam')
# else:
#     print('Wonderful, You are eligible for sitting in exam')

#ex:1
for i in range(-100, -9,10):
    print(i, end=',')

#ex : 2

prime_list= [ ]
for i in range(10, 20):
    count = 0
    for j in range(1, i +1):
        if i % j == 0:
            count = count + 1
    if count == 2:
        print(i)
        prime_list.append(i)

print(prime_list)
sum =0
for val in prime_list:
    sum = sum + val
print(sum)

total = 0
index = 0
while (index < len(prime_list)):
    total = total + prime_list[index]
    index =index + 1
    
print(total)

for i in range(9, 0, -2):
    print(i) 

data = 'i love data science so much'

while i<len(data):
    print(data[i])
    i = i + 1
    
data = data.split()
i = 0
while i<len(data):
    print(data[i])
    i = i + 1
print('Crazy',data[-3])

L_list = ['ai', 3, 'studymart', 7, 8, 'Ml']
print(L_list.pop())
print(L_list.append(3))
print(L_list)
print(L_list.pop(1))
print(L_list)
#comprehension list
list1 = [x for x in range(10)]
print(list1)
list1 = [ x for x in range(10) if x % 2 == 0]
print(list1)
print(10 in list1)

tu1 = ('run', 4 , 's')
tu2 = ('sif',)
print(type(tu1))
T_list = list(tu1)
print(type(T_list))
T_list.append('add')
print(T_list)
tu1 = tuple(T_list)
print(type(tu1))
print(tu1 + tu2 )
set1 = {(1, 5,7), 5, 'ai', True}
print(set1)
set1.add(100)
print(set1)
set1.update([10, 20, 50, 100 ,20])#update is used for multiple add
print(set1)
set1.remove(20)#romove function works when the value exist in the set. otherwise it show error
print(set1)
print(set1.discard(20))
set2 = {(1, 5,7), 5, 'ai', True}
set3 = {(1, 5,7), 8, 12, 5, 'ai', False}
s1 = frozenset(set2)
print(type(s1))
s2 = frozenset(set3)
print(s1.union(s2))
print(s1.intersection(s2))
s3 = frozenset('data science')
print([ list(x) for x in s3 ] )
print(s1.difference(s2))
print(s2.difference(s1))

