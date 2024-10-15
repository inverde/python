# Make function module for conditional samples
c_YES = 'yes'
c_NO = 'no'

# Get vote from citizen
def supporting_ballot():
    global c_YES
    vote = input("Do you agree with this reform?: ")
    if vote == c_YES:
        return True
    else:
        return False
# Get case insensitive answer  and clean white spaces
def std_supporting_ballot():
    global c_Yes
    vote = in

if supporting_ballot():
    print("Plus Vote")
else:
    print("Minus Vote")
