import conditionals as condMod
# Alternative execution happens when conditional statements brake into two branches
def main():
    n = get_number()
    if is_even(n):
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

    # This is a phytonic call
    print('Number classification:',
          alternative_execution(n, n % 2 == 0, lambda x: f"{n} is even", lambda x: f"{n} is odd"))


def get_number():
    while True:
        x = int(input("Por favor digite un numero entero:? "))
        if x > 0:
            break
        else:
            continue
    return x

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


# Define a function to classify number between even and odd -- Only two altenative.
def alternative_execution(n, test, main, alternate):
    if test:
        # main branch executes main parameter function
        return main(n)
    else:
        #alternate branch executes alternate parameter function
        return alternate(n)

condMod.set_testing(condMod.c_OFF)

if __name__ == "__main__":
    if condMod.is_testing():
        main()


