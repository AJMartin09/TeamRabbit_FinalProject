#movie.py
# Name: Andrew Martin, Aanika Garre, Joseph Rainford
# email: marti6aj@mail.uc.edu, garreaa@mail.uc.edu, rainfojp@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23rd, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
''' Brief Description of the assignment: TBD TBD'''

# Brief Description of what this module does: Decrypt's the first encrypted message to reveal the location needed
# Citations:
# Anything else that's relevant:

import json
from cryptography.fernet import Fernet

def load_movies(file_path):
    '''
    TBD
    '''
    with open(file_path, "r") as file:
        data = json.load(file)
        rabbitData = data.get("Rabbit")
    return rabbitData
    
def decrypt_movies():
    '''
    TBD
    '''
    password = "PASSWORDHERE from Prof"
    cipherSuite = Fernet(password)
    decodedTitle = cipherSuite.decrypt(rabbitData)
    print(decodedTitle)
    print(decodedTitle)
    print()

if __name__ == "__main__":
    load_movies("TeamsAndEncryptedMessagesForDistribution - 001.json")
    decrypt_movies()
    