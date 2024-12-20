# MODULE 12 LAB: CREATE A PET CLASS
#
# David Vance
# Professor Kevin Chang
# CIS129 - Programming and Problemsolving I
# 18 October 2024
"""This module creates a Pet Class, to include the pet's name, type, and age.
Once the class is designed, the module creates an object of the class, then 
prompts the user for information to be stored in that class.  Finally, this 
information needs to be accessed through the object's accesssor methods and 
displayed to the screen."""

# INITIATIONS
# Import modules, declare CONSTANTS, set variables, build dictionaries and 
# build classes

from colorama import Fore, Back, Style # This allows colorized text

# Build the Pet class and include accessor methods
class Pet:
    """A pet with a name, type and age"""

    def __init__(self, pet_name, pet_type, pet_age):
        """Initialize basic pet attributes."""
        self._pet_name = pet_name
        self._pet_type = pet_type
        self._pet_age = pet_age

    @property
    def pet_name(self):
        return self._pet_name

    @property
    def pet_type(self):
        return self._pet_type
    
    @property
    def pet_age(self):
        return self._pet_age 
    
    def __repr__(self):
        """Return string representation for repr()."""
        return (f'Your pet name: {self.pet_name}\n' +
                f'Your pet type: {self.pet_type}\n' +
                f'Your pet age:  {self.pet_age}\n')
    

# MAIN PROCESSING

def main():
    # constructor pet of class Pet
  
    MyPet = Pet(str(input("Enter your pet's name:\n")),
                 str(input("Enter your pet's type:\n")),
                 int(input("Enter your pet's age:\n")))       
    
    print(Fore.GREEN)  #Set Green as the text color for MyPet info
    print(MyPet)

    print(Fore.YELLOW + '-----')  # Set Yellow as the color for the closing banner
    print('Thank you for using PetMaster.')
    print('We hope to see you soon!' + Fore.WHITE)  # Set Text color back to White

if __name__ == '__main__':
    main()
