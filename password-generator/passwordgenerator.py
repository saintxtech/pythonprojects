import random
import string
print("Welcome to the Password Generator!")

# Ask for password length
length_input = input("Enter desired password length: ")

# Convert to integer and validate
try:
    length = int(length_input)
    if length <= 0:
        print("Password length must be greater than 0.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

# Ask for character set preferences
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
use_numbers = input("Incude numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

#Build character pool based on user preferences
characters = ""
if use_uppercase:
    characters += string.ascii_uppercase
if use_lowercase:
    characters += string.ascii_lowercase
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

#Validate that at least one character type was chosen
if not characters:
    print("You must select at least one chracter type.")
    exit()

# Use random.choices to generate a list of characters
password = ' '.join(random.choices(characters, k=length))

print(f"\nYour generated password is:\n{password}")