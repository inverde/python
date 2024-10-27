names = []

def get_name():
    while True:
        try:
            return input("What's your name:? ")
        except ValueError:
            continue
def main():
    with open("names.txt", 'a') as file:
        for _ in range(3):
            name = get_name()
            file.write(f"{name}\n")
            names.append(name)
        for name in names:
            print(name)

def load_names():
    pass

if __name__ == "__main__":
    # todo Implements the load_names function
    main()

