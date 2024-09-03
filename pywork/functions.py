def hello():
    print("Functions Hello!")

hello()

def sum(num1, num2):
    return num1+num2

result = sum(2,3)
print(result)

def multi_items(*args):
    print(args)
    print(type(args))

multi_items("Ram",10)

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(name = "Ram",age = 40)