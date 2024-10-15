# Make function module for conditional samples
c_YES = 'yes'
c_NO = 'no'

# Define vote
def supporting_ballot():
    global c_YES
    vote = input("Do you agree with this reform?: ")
    if vote == c_YES:
        return True
    else:
        return False

if supporting_ballot():
    print("Plus Vote")
else:
    print("Minus Vote")
