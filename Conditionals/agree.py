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
globals = {}
globals['STD_BALLOT'] = c_TRUE
globals['NOR_BALLOT'] = c_FALSE
globals['VOTING_SYSTEM'] = c_STD
#------------------------------------------------------------------------------

def set_std_ballot(toggle= c_TRUE):
    global globals
    globals['STD_BALLOT'] = toggle

def is_std_ballot():
    global globals
    return globals['STD_BALLOT']

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
    globals['VOTE'] = std_supporting_ballot()
else:
    globals['VOTE'] = supporting_ballot()

# Voting pro and against with either of the ballots
if (is_std_ballot() and globals['VOTE']) or (not is_std_ballot() and globals['VOTE']):
    print("Plus Vote")
elif (is_std_ballot() and not SUPPORTING_VOTE[c_STD]) or (not is_std_ballot and not SUPPORTING_VOTE[c_NOR]):
    print("Minus Vote")

