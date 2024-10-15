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
globals['STD_VOTE'] = None
globals['NOR_VOTE'] = None
globals['TEST'] = c_OFF
#------------------------------------------------------------------------------

def set_std_ballot(toggle= c_TRUE):
    global globals
    globals['STD_BALLOT'] = toggle

def set_testing(toggle=c_ON):
    global globals
    globals['TEST'] = toggle

def is_testing():
    global globals
    if globals['TEST'] == c_ON:
        return True
    else:
        return False

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

def std_supporting_ballot():
    global c_Yes
    vote = input("Do you agree with this reform?: ")
    if vote.lower().startswith('y') or (vote.strip().lower() == c_YES):
        return True
    else:
        return False


# Set standard ballot for this election
set_std_ballot()

# Set the module in testing mode
set_testing()


# Voting pro or against a constitutional reform
def cast_vote():
    if is_std_ballot():
        globals['STD_VOTE'] = std_supporting_ballot()
    else:
        globals['NOR_VOTE'] = supporting_ballot()

    if (is_std_ballot() and globals['STD_VOTE']) or (not is_std_ballot() and globals['NOR_VOTE']):
        print("Plus Vote")
    elif (is_std_ballot() and not globals['STD_VOTE']) or (not is_std_ballot and not globals['NOR_VOTE']):
        print("Minus Vote")

def test():
    if is_testing():
        set_std_ballot()
        cast_vote()
        cast_vote()
        cast_vote()
        cast_vote()
        set_std_ballot(c_FALSE)
        cast_vote()
        cast_vote()
        cast_vote()
        cast_vote()

if __name__ == "__main__":
    test()
