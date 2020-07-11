# Voting Machine
#
# Authors: Victor Torres and Maxwell Rahmani
# Version:
# Description: Commandline interface for the application
# Note: A lot of error handling is done here
#
#
#

# ----------------------------------------------------------------- #

# Imports ----------
import voter_framework.py
import time

voter = Vote("","","","","")

# Will dispay info to the user about about whatever
def displayInfo():
    print(voter)

    # Gets the voter ID and PIN from the user
def getVoterCreds():

    try:
            first,last = input("Who are you? enter name").split()
            pin = input("What is your pin?")
            #do we reference input before adding to voter object?

        pass
            voter.FIRSTNAME = first
            voter.LASTNAME = last
            voter.VOTER_PIN = pin
            voteCast()
    except Exception as e:
        raise
            print("Not a valid info")

    print()

    # Prompts the user for their vote
def voteCast():
        # this can change when you are allowed to create custom voting practices
        # TODO: need a dynamic way to allow more than 5 votes
            # can use a JSON to handle some basic settings like this
            # inluding number of things you are choosing from, their names etc
        #choice = Vote_choice("","")

    options = []
    ranking = [1,2,3,4,5]
    usrVote = []

    print("You will be ranking the following:" + options)

    # Will probably need to break the stuff below out into its own function that accepts an integer
    # error checking on this line

    usrChoice1 = 0
    for x in options:
        while usrChoice1 not in options:
            usrChoice1 = input("Please rank" + x + ":")
        options.remove(usrChoice1)
        usrVote.append(usrChoice1)

    officialVote = usrVote

        #need prompt listed votes Casted
        # need to have a list of items and a list of vote rankings
        #vote = input("place votes" + items + vote) here need to know how ranking is gonna be taken

    voter.TIMESTAMP = time.ctime(time.time())
