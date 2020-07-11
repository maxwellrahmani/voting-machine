# Voting Machine Application
****
## Goal: To create a safe rank by choice voting application that has high error checking without sacrificing usability by the voter.

### Main Priorities:
- Safety
- Ease of use
- verifiable results



### File System requirements:
- Write only
- Nothing is written to the file system without rigorous error checking
- Possible encryption of a vote so that data is not readable
  - Hash Keys maybe?
  - Data that will be written to a database will be in hash format
-

### Vote Verification
- 1 Vote = Name/Voter ID, Choices (1-5), Voter PIN?(some kind of ID), timestamp
- What does a vote look like? See "#1 Vote"



### requirements.txt
- used to download any dependencies
- USAGE ```pip install -r requirements.txt```


### Functionality
- When application is open Verification of person is needed. Once checked next page
- Title of what you are voting for. and options. this will be ranked by choice.


# Files

## db.py
**Functions**:
