# Make function module for conditional samples
c_YES = 'yes'
c_NO = 'no'

# Define vote
def supporting_ballot(on_support = c_NO):
    if on_support == c_YES:
        return True
    else:
        return False
