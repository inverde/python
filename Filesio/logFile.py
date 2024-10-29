# In this program will be logging messages to a debug file

def openFile(filename, mode):
    return open(filename, mode)

def closeFile(file):
    file.close()

file = openFile("log.txt", 'a')

file.write("Logging debug messages to my file\n")

print(type(file))

closeFile(file)
