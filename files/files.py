# r = Read
# a = Append
# w = Write
# x = Create

import os

# Read - Error if it doesn't exist

f = open("/Users/dhyana/Documents/PythonProject/files/names.txt")
# print(f.read())
# print(f.read(4))
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("/Users/dhyana/Documents/PythonProject/files/names.txt")
    print(f.read())
except:
    print("File doesnt exist")
finally:
    f.close()

# Append - Creates the file if it doesnt exist

f = open("/Users/dhyana/Documents/PythonProject/files/names.txt", "a")
f.write("Dave\n")
f.close()

f = open("/Users/dhyana/Documents/PythonProject/files/names.txt")
print("***APPEND***")
print(f.read())
f.close()

# Write - Overwrite
f = open("/Users/dhyana/Documents/PythonProject/files/context.txt", "w")
f.write("All context deleted")
f.close()

f = open("/Users/dhyana/Documents/PythonProject/files/context.txt")
print("***WRITE***")
print(f.read())
f.close()

# Two ways to create new file

# Opens a file for writing, creates the file if it doesn't exist

f = open("/Users/dhyana/Documents/PythonProject/files/name_list.txt", "w")
f.close()

# Creates the specified file but returns an error if file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt","x")
    f.close()

# Delete a file

# avoid an error if it doesnt exist

if os.path.exists("dave.txt"):
    print("***DELETE***")
    os.remove("dave.txt")
else:
    print("The file to delete doesn't exist")

with open("/Users/dhyana/Documents/PythonProject/files/more_names.txt") as f:
    content = f.read()

with open("/Users/dhyana/Documents/PythonProject/files/names.txt","w") as f:
    f.write(content)