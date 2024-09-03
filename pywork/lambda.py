squared = lambda num: num * num
print(squared(2))

addtwo = lambda num: num + 2
print(addtwo(13))

sumTotal = lambda a, b: a + b
print(sumTotal(4,5))

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(f"addTen: {addTen(7)}")
print(f"addTwenty: {addTwenty(7)}")

####################################
numbers = [3,6,7,18,15,26]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

####################################
odd_nums = filter(lambda num: num % 2 != 0,numbers)

print(list(odd_nums))

####################################

from functools import reduce

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr,numbers)

print(total)
print(sum(numbers,10))

####################################
names = ["Ram Paul", "Dhyana Ram", "Dave Gray", "Joey Francis Tribbiani"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)