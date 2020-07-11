# Voting Machine
#
# Authors: Victor Torres and Maxwell Rahmani
# Version:
# Description: File Dedicated to the framwork of the voting data scructure
# Note:
#
#
#

# ----------------------------------------------------------------- #


# Imports ----------
import os.path
from os import path
import csv  # surprise surprise
import time # used for creating the timestamp
import crypography
from cryptography.fernet import Fernet



def submitToDB():



def filePrep():
    # check if file exists
        # do Nothing
    # if false then
        # write vote and keys file



# Encrypts the vote into a hash before writing to file
def encryptVote(Vote v):
    key = Fernet.generateKey()
    temp_write = [v.VOTER_ID, key]

    with open('data/keys.csv', mode = 'a') as key_file:
        encWriter = csv.writer(key_file)
        encWriter = csv.writerow(temp_write)

    vote = processVote(v)

    return item


# Converts a list into a comma separated string
def listToString(l):
    str = ""
    for element in l:
        str += (element + ",")
    return str

def processVote(Vote v):
    processed = v.VOTER_ID + "," + v.LASTNAME + "," + v.FIRSTNAME + ","
    + listToString(v.VOTE)

    return processed



# Appends a vote to the 'votes.csv' file
# is privilege checking happening here or another function?
def appendVote(encryptedVote v):
    with open('data/votes.csv', mode = 'a') as voter_file:
