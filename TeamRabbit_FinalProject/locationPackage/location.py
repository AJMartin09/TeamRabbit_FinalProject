#location.py
# Name: Andrew Martin, Aanika Garre, Joseph Rainford
# email: marti6aj@mail.uc.edu, garreaa@mail.uc.edu, rainfojp@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23rd, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Decrypt two encrypted messages to reveal a location and a movie title so that
                                    #  we can take a picture in the given location with a quote from the given movie.

# Brief Description of what this module does: Decrypt's the first encrypted message to reveal the location needed
# Citations:
# Anything else that's relevant:

def load_words(file_path):
    """
    Load the encrypted words from the provided file path.
    """
    with open(file_path, "r") as file:
        return [word.strip() for word in file]

def assemble_location(indices, words):
    """
    Decrypt the location using the provided indices.
    """
    decrypted_location = " ".join(words[int(index)] for index in indices)
    return decrypted_location

if __name__ == "__main__":
    words = load_words("UCEnglish.txt")
    
    # Indices provided for Team Rabbit
    indices = ["30942", "42547", "19312", "65919", "8879", "36488", "2756", "45854", "18755", "28894", "8018", "2756", "24979", "42636"]
    
    # Decrypt the code to reveal the location
    decrypted_location = assemble_location(indices, words)
    print(f"Assembled location: {decrypted_location}")
 
