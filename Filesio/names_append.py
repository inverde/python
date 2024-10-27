for _ in range(3):
    name = get_name()
    file = open("names.txt", 'a')
    file.write(name)

file.close()
