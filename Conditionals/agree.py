# Make function module for conditional samples

# Define constants to be used agree module --------------------------------
c_YES = 'yes'
c_NO = 'no'

c_TRUE = True
c_FALSE = False

c_ON = 'on'
c_OFF = 'off'
#-------------------------------------------------------------------------

# Declare global variables for this module ----------------------------------
STD_BALLOT = {}
#------------------------------------------------------------------------------

def set_std_ballot(toggle= c_TRUE):
    global STD_BALLOT
    if toggle:
        STD_BALLOT[c_ON] = toggle
        STD_BALLOT[c_OFF] = not toggle
    else:
        STD_BALLOT[c_OFF] = toggle
        STD_BALLOT[c_ON] =  not toggle

def is_std_ballot():
    global STD_BALLOT
    global c_ON
    if STD_BALLOT[c_ON] == True:
        return True
    else:
        return False

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


# Set standard ballot for this election
set_std_ballot()

if (is_std_ballot() and std_supporting_ballot()) or (not is_std_ballot() and supporting_ballot()):
    print("Plus Vote")
elif (is_std_ballot and not std_supporting_ballot()) or (not is_std_ballot and not supporting_ballot()):
    print("Minus Vote")


# Vote with normal ballot
if supporting_ballot():
    print("Plus Vote")
else:
    print("Minus Vote")
# Vote with standar ballot
if std_supporting_ballot():
    print("Plus Vote")
else:
    print("Minus Vote")
