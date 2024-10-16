# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import ../Conditionals/conditionals as condMod
# Sometimes we need to send a message several times
"""Lets write a litle program for the cat
"""
condMod.set_testing(condMod.c_OFF)

def main():
    repeat("meaow", 3)

if condMod.is_testing():
    print("meaow")
    print("meaow")
    print("meaow")

# Define a function to print any message n times instead of three
"""Our function repeat msg need to use the structure of a loop
"""
def repeat(msg, times):
    # Test with1
    # while loop
    n = times
    while n:
        print(msg)
        n-= 1

main()
