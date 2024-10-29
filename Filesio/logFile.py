# In this program will be logging messages to a debug file

def openFile(filename, mode):
    return open(filename, mode)

file = openFile("log.txt", 'a')

print(type(file))

file.close()
