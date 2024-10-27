names = []

def get_name():
    while True:
        try:
            return input("What's your name:? ")
        except ValueError:
            continue

for _ in range(3):
    name = get_name()
    file = open("names.txt", 'a')
    file.write(name)
    names.append(name)
    file.close()

for name in names:
    print(name)

