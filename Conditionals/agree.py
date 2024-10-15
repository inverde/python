# Make function module for conditional samples
c_YES = 'yes'
c_NO = 'no'

c_TRUE = True
c_FALSE = False

c_STD_BALLOT = None


def set_std_ballot(on= c_TRUE):
    if on:
        c



# Get vote from citizen
def supporting_ballot():
    global c_YES
    vote = input("Do you agree with this reform?: ")
    if vote == c_YES:
        return True
    else:
        return False

# Get case insensitive vote  and clean white spaces
def std_supporting_ballot():
    global c_Yes
    vote = input("Do you agree with this reform?: ")
    if vote.strip().lower() == c_YES or vote.strip().lower().startwith == 'y':
        return True
    else:
        return False


if supporting_ballot():
    print("Plus Vote")
else:
    print("Minus Vote")

if std_supporting_ballot():
    print("Plus Vote")
else:
    print("Minus Vote")
