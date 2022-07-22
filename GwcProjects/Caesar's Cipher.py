# Global variables
possible_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
initial_position = 0
shifted_position = 0
shifted_message = ""

# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. "
      "\n\nWhen creating your message, you may only choose from the following characters: " + possible_characters +
      "\n\nLet's get started!\n")

# Receive user input
initial_message = input("What is your message? ")
key = int(input("What is the key? Choose a number from 0 to 25. "))
mode = input("Do you want to encrypt or decrypt? ")

# Encrypt or decrypt the message
for character in initial_message:
    if character in possible_characters:
        initial_position = possible_characters.find(character)

        if mode.lower() == "encrypt":
            shifted_position = initial_position + key
        elif mode.lower() == "decrypt":
            shifted_position = initial_position - key

        if shifted_position >= len(possible_characters):
            shifted_position -= len(possible_characters)
        elif shifted_position < 0:
            shifted_position += len(possible_characters)

        shifted_message += possible_characters[shifted_position]

    else:
        shifted_message += character

# Print the shifted message
print("Your " + mode.lower() + "ed message is: " + shifted_message)
