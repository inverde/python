# In this program will be logging messages to a debug file

# Please write a decorator functions to help trace my code when logging
def traceOpen(func):
    def wrapper(arg1, arg2):
        print(f"Before calling {func.__name__}")
        resultado = func(arg1, arg2)
        print(f"After calling {func.__name__}")
        return resultado
    return wrapper

def traceCall(func):
    def wrapper():
        print(f"Before calling {func.__name__}")
        func()
        print(f"After calling {func.__name__}")
    return wrapper
#-----------------------------------------------------------------------------------

@traceOpen
def openFile(filename, mode):
    return open(filename, mode)

@traceClose
def closeFile():
    global file
    file.close()

def printio(message):
    global file
    file.write(message + '\n')


file = openFile("log.txt", 'a')

printio("Logging debug messages to my file")
printio("Testing for a second line of degug messages")

print(type(file))

closeFile()

