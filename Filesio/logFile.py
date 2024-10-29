# In this program will be logging messages to a debug file

# Please write a decorator function to help trace my code when testing
def traceCall(func):
    def wrapper():
        print("Before calling {func.__name__}")
        func()
        print("After calling {func.__name__}")
    return wrapper

@traceCall
def openFile(filename, mode):
    return open(filename, mode)

@traceCall
def closeFile(file):
    file.close()

file = openFile("log.txt", 'a')

file.write("Logging debug messages to my file\n")
file.write("Testing for a second line of degug messages\n")

print(type(file))

closeFile(file)

