names[]

for _ in range(3):
    name = input("What's your name:? ")
    file = open("names.txt", 'a')
    file.write(name)
    names.append(name)
    file.close()
