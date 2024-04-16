#movie.py

# Name: Andrew Martin, Aanika Garre, Joseph Rainford
# email: marti6aj@mail.uc.edu, garreaa@mail.uc.edu, rainfojp@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23rd, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
#Brief Description of the sssignment: Decrypt two encrypted messages to reveal a location and a movie title so that
                                    #  we can take a picture in the given location with a quote from the given movie.

# Brief Description of what this module does: Decrypts the second encrypted message to reveal the movie assigned
# Citations:
# Anything else that's relevant:

import json

from cryptography.fernet import Fernet

def load_movies():
   '''
   Decrypts the movie using the password provided by the professor
   @return: Decrypted movie name
   '''
   file_path = "../TeamsAndEncryptedMessagesForDistribution - 001.json"
   with open(file_path, "r") as file:
       data = json.load(file)
       rabbitData = str(data.get("Rabbit"))
       rabbitDataByte = bytes(rabbitData, "utf-8")
   password = str("LMV69IGGTp2Gyn4TI-DTuupf0VvugeC5API5dpeoiqM=")
   f = Fernet(password)
   decodedTitle = f.decrypt(rabbitDataByte)
   print(decodedTitle)

if __name__ == "__main__":

   load_movies()