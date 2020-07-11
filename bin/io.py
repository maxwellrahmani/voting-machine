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

voter = Vote("","","","","")
while Continue == True:

    # Will dispay info to the user about about whatever
    def displayInfo():
        print()

    # Gets the voter ID and PIN from the user
    def getVoterCreds():
        # cross reference input with the database of voterIDs for validation
        try:
                first,last = input("Who are you? enter name").split()
                voter.FIRSTNAME = first
                voter.LASTNAME = last
                pin = input("What is your pin?")
                voter.PIN = pin
            pass
                voteCast()
        except Exception as e:
            raise
                print("Not a valid info")



        print()

    # Prompts the user for their vote
    def voteCast():
        # this can change when you are allowed to create custom voting practices
        # TODO: need a dynamic way to allow more than 5 votes
        ranking = [1,2,3,4,5]
        #need prompt listed votes Casted
        # need to have a list of items and a list of vote rankings
        #vote = input("place votes" + items + vote)
        voting = input("what rank is " + ranking + " is blue") #testing need to change to items
        try:

            pass
        except Exception as e:
            raise
        else:
            pass

    #
