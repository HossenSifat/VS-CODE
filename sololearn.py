#list
bikes = ['trek', 'redline', 'giant']
print(bikes[0])
bikes.append('scoty')
print(bikes)
bikes.insert( 1, 'royal')
print(bikes)
bikes.remove('scoty')
print(bikes)
del bikes[3]
print(bikes)
bikes.pop()
print(bikes)
bikes.pop(0)
print(bikes)

Desi_bikes = ['redline', 'ayle','giant', 'bigi', 'Aile', 'Bitter']
# print(sorted(Desi_bikes))
# print(sorted(Desi_bikes, reverse=True))
bikee = Desi_bikes.sort()
print(bikee)


for bike in bikes:
    print(bikes)
square = []
for x in range(1, 11):
    square.append(x**2)
print(square)
square= [x**2 for x in range(1,11)]
print(square)

#function
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5 
print(apply_twice(add_five, 10 ))