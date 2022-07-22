import string

# Global variables
initial_position = 0
shifted_position = 0
shifted_message = ""
letters_lower = string.ascii_lowercase
letters_upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
possible_characters = letters_lower + letters_upper + numbers + symbols


# Define the function called encryptOrDecrypt
def encrypt_or_decrypt():
    global shifted_position
    if mode.lower() == "encrypt":
        shifted_position = initial_position + key
    elif mode.lower() == "decrypt":
        shifted_position = initial_position - key


# Define the function called wraparound
def wrap_around():
    global shifted_position
    if shifted_position >= len(possible_characters):
        shifted_position = shifted_position - len(possible_characters)
    elif shifted_position < 0:
        shifted_position = shifted_position + len(possible_characters)


# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. "
      "\n\nWhen creating your message, you may only choose from the following characters: " + possible_characters +
      "\n\nLet's get started!\n")

# Receive user input
initial_message = input("What is your message? ")
key = int(input("What is the key? Choose a number from 0 to 93. "))
mode = input("Do you want to encrypt or decrypt? ")

# Encrypt or decrypt the message
for character in initial_message:
    if character in possible_characters:
        initial_position = possible_characters.find(character)

        encrypt_or_decrypt()

        wrap_around()

        shifted_message += possible_characters[shifted_position]

    else:
        shifted_message += character

# Print the shifted message
print("Your " + mode.lower() + "ed message is: " + shifted_message)
