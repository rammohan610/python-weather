name = "Ram"
count = 1

def greeting(name):
    print(name)
    global count
    count = 3
    print (count)

greeting("Dhyana")
print(name)
print(count)