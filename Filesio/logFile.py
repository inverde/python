# In this program will be logging messages to a debug file

# Please write a decorator functions to help trace my code when logging
def traceOpen(func):
    def wrapper(arg1, arg2):
        print(f"Before calling {func.__name__}")
        resultado = func(arg1, arg2)
        print(f"After calling {func.__name__}")
        return resultado
    return wrapper

def traceClose(func):
    def wrapper(arg1):
        print(f"Before calling {func.__name__}")
        func(arg1)
        print(f"After calling {func.__name__}")
    return wrapper
#-----------------------------------------------------------------------------------

@traceOpen
def openFile(filename, mode):
    return open(filename, mode)

@traceClose
def closeFile(file):
    file.close()

def printio

file = openFile("log.txt", 'a')

file.write("Logging debug messages to my file\n")
file.write("Testing for a second line of degug messages\n")

print(type(file))

closeFile(file)

