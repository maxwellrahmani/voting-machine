# Voting Machine
#
# Authors: Victor Torres and Maxwell Rahmani
# Version:
# Description: Object Handler for the VOTE object
# Note:
#
#
#

# ----------------------------------------------------------------- #


# Imports
import time


# VOTE object
class Vote:
    def __init__(voter,FIRSTNAME,LASTNAME,VOTER_PIN,TIMESTAMP,VOTE)
    voter.VOTER_PIN = VOTER_PIN
    voter.LASTNAME = LASTNAME
    voter.FIRSTNAME = FIRSTNAME
#VOTE needs to change to a list
    voter.VOTE = VOTE
    voter.TIMESTAMP = TIMESTAMP

# ENCTRYPTED VOTE Object
class EV:
    def __init__(ev, ID, VALUE, TIMESTAMP)
    ev.ID = ID
    ev.VALUE = VALUE
    ev.TIMESTAMP = TIMESTAMP
