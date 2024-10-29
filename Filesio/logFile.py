# In this program will be logging messages to a debug file

def openFile(filename, mode):
    return open(filename, mode)

def closeFile(file):
    file.close()

file = openFile("log.txt", 'a')

print(type(file))

