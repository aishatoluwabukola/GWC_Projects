import string

# Global variables
initial_position = 0
shifted_position = 0
lettersLower = string.ascii_lowercase
lettersUpper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
possible_characters = lettersLower + lettersUpper + numbers + symbols


# Define the function called decrypt
def decrypt():
    global shifted_position
    shifted_position = initial_position - key


# Define the function called wraparound
def wraparound():
    global shifted_position
    if shifted_position < 0:
        shifted_position += len(possible_characters)


# Run code

# Introduction
print("Welcome! This program will crack the Caesar cipher and figure out any secret message that was encrypted with the"
      " Caesar cipher. Type in your encrypted message and this program will print all of the key possibilities of your "
      "message below. \n\nYour message can only include the following characters: " + possible_characters + "\n\n")

# Receive user input
initial_message = input("What is your encrypted message? ")
input("\nPress enter to generate all of the key possibilities for your encrypted message.\n")

# Cycle through all possible keys
for key in range(len(possible_characters)):
    shifted_message = ""
    # Decrypt the message
    for character in initial_message:
        if character in possible_characters:
            initial_position = possible_characters.find(character)
            decrypt()
            wraparound()

            shifted_message += possible_characters[shifted_position]

        else:
            shifted_message += character

    # Print the shifted message
    print("Key #{0}: {1}.".format(key, shifted_message))

# Closing message
print("\nNow scroll through all of the key possibilities above and find the readable plaintext message.")
