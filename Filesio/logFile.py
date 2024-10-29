# In this program will be logging messages to a debug file

# Please write a decorator function to help trace my code when testing
def traceCall(func):
    def wrapper(arg1, arg2):
        print(f"Before calling {func.__name__}")
        resultado = func(arg1, arg2)
        print(f"After calling {func.__name__}")
        return resultado
    return wrapper

@traceCall
def openFile(filename, mode):
    return open(filename, mode)
def closeFile(file):
    file.close()

file = openFile("log.txt", 'a')

file.write("Logging debug messages to my file\n")
file.write("Testing for a second line of degug messages\n")

print(type(file))

closeFile(file)

