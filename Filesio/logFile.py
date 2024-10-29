# In this program will be logging messages to a debug file

# Please write a decorator function to help trace my code when testing
def traceCall(func):
    def wrapper():
        printio("Before calling {func.__name__}")
        func()

def openFile(filename, mode):
    return open(filename, mode)

def closeFile(file):
    file.close()

file = openFile("log.txt", 'a')

file.write("Logging debug messages to my file\n")
file.write("Testing for a second line of degug messages\n")

print(type(file))

closeFile(file)

