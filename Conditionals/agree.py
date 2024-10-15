# Make function module for conditional samples

# Define constants to be used agree module --------------------------------
c_YES = 'yes'
c_NO = 'no'

c_TRUE = True
c_FALSE = False

c_ON = 'on'
c_OFF = 'off'

c_STD = 'standard'
c_NOR = 'normal'
#-------------------------------------------------------------------------

# Declare global variables for this module ----------------------------------
STD_BALLOT = {}
SUPPORTING_VOTE = {}
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
    if vote.lower().startswith('y') or (vote.strip().lower() == c_YES):
        return True
    else:
        return False


# Set standard ballot for this election
set_std_ballot()

if is_std_ballot():
    SUPPORTING_VOTE[c_STD] = std_supporting_ballot()
    SUPPORTING_VOTE[c_NOR] = not SUPPORTING_VOTE[c_STD]
else:
    SUPPORTING_VOTE[c_NOR] = supporting_ballot()
    SUPPORTING_VOTE[c_STD] = not SUPPORTING_VOTE[c_NOR]

# Voting pro and against with either of the ballots
if (is_std_ballot() and SUPPORTING_VOTE[c_STD]) or (not is_std_ballot() and SUPPORTING_VOTE[c_NOR]):
    print("Plus Vote")
elif (is_std_ballot() and not SUPPORTING_VOTE[c_STD]) or (not is_std_ballot and not SUPPORTING_VOTE[c_NOR]):
    print("Minus Vote")

