#photo.py
# Name: Andrew Martin, Aanika Garre, Joseph Rainford
# email: marti6aj@mail.uc.edu, garreaa@mail.uc.edu, rainfojp@mail.uc.edu
# Assignment Number: Final Project
# Due Date: April 23rd, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Decrypt two encrypted messages to reveal a location and a movie title so that
                                    #  we can take a picture in the given location with a quote from the given movie.

# Brief Description of what this module does: Loads and displays photo take at location decrypted with quote from movie decrypted
# Citations:
# Anything else that's relevant:

from PIL import Image

def load_and_display_image():
    '''
    Loads and displays photo taken at decrypted location with decrypted movie quote
    @return: Photo of group members at Chick-Fil-A with a quote from Jurassic Park
    '''
    image_path = "../IMG_7627.JPG"
    img = Image.open(image_path)
    final_image = img.rotate(-90)
    final_image.show()
    
if __name__ == "__main__":
    load_and_display_image()
    