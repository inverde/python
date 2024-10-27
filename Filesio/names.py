names[]

for _ in range(3):
    name = input("What's your name:? ")
    file = open("names.txt", 'a')
    file.write(name)
    names.append(name)
    file.close()

    """Program weakness
        1. Do not catch error for user input
        2. Every time writes to file must open it and close it
    """
