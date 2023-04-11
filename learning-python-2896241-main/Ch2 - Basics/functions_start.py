#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def basicFunc():
    print("I am a FUNCTION")


# TODO: function that takes arguments
def argsFunc(arg1, arg2):
    print(arg1, " ", arg2)

# TODO: function that returns a value
def returnSometing(x):
    return x * x * x


# TODO: function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# TODO: function with variable number of arguments
def numArgsFunc(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(numArgsFunc(6,4,6,3,2,6,8))

# basicFunc()
# print(basicFunc())
# print(basicFunc)

# argsFunc(10, 20)
# print(argsFunc(10, 20))
# returnSometing(3)

# print(power(2))
# print(power(2, 3))
# print(power(2))