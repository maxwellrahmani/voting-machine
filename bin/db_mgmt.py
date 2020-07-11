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

# Submits a vote to the CSV database
def submitToDB(Vote v):
    ev = encryptVote(v)
    appendVote(ev)

# Ensures appropriate files exist
def fileCheck():


    # check if file exists # do Nothin # if false then # write vote and keys file
    return val

# Appends a vote to the 'votes.csv' file
def appendVote(encryptedVote ev):
    to_write = [ev.ID, ev.VALUE, ev.TIMESTAMP]
    with open('data/votes.csv', mode = 'a') as voter_file:
        vote_writer = csv.writer(voter_file)
        vote_writer = csv.writerow(to_write)


# Encrypts the vote into a hash before writing to file
def encryptVote(Vote v):
    key = Fernet.generate_key()
    temp_write = [v.VOTER_ID, key]

    with open('data/keys.csv', mode = 'a') as key_file:
        encWriter = csv.writer(key_file)
        encWriter = csv.writerow(temp_write)

    vote = processVote(v)
    vote = vote.encode()
    e = Fernet(key)
    tempEnc = e.encrypt(vote)

    ev = encryptedVote(v.VOTER_ID, tempEnc, v.TIMESTAMP)
    return ev


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
