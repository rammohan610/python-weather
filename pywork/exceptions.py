# refer w3schools website for built in exceptions for python
class JustNotCool(Exception):
    pass

x = 2
s = "Ram"
try:
    raise JustNotCool("This isn't cool")
    # raise Exception("I am a custome Exception")
    # print(x / 2)
    # if not type(x) is str:
    #     raise TypeError("Only Strings are allowed")
    
except NameError:
    print("NameError occured. Something is undefined")

except ZeroDivisionError:
    print("ZeroDivisionError occured. Please do not divide by zero")

except Exception as error:
    print(error)

else:
    print("No Erros")

finally:
    print("I am Inevitable")