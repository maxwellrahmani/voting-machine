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
# TODO: find list pairs or change to Vote_choice Object
    voter.VOTE = VOTE
    voter.TIMESTAMP = TIMESTAMP

#made this since I did not know how to do list pairs
class Vote_choice:
    def __init__(choice,rank,item)
    choice.rank = rank
    choice.item = item
