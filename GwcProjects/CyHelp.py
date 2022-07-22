print("Hello! I'm CyHelp.")
user_name = input("What is your name?\n")
print("\nNice to meet you " + user_name + ".")

# Recounts start of Cybersecurity
cybersecurity_birth_year = 1970
todays_year = input("What year is it?\n")
time_passed = int(todays_year) - cybersecurity_birth_year

print("\nWow! That means it has been " + str(time_passed) + " years since Cybersecurity began!")
print("The field of Cybersecurity started in the 1970s when more and more information started "
      "being stored on computer systems and networks!")
input("Press enter to continue.\n")

# Describes Cybersecurity
print("Cybersecurity refers to the practices and techniques that people use to protect computer systems "
      "and networks from digital threats.")
print("These people can be government, nations, individuals, companies, community organizations and hackers.\n")

print("The cybersecurity field has expanded to far more than just protecting our smartphones and computers."
      "\nI think smart locks are cool. I'm sure you do too but have you ever stopped to think about how this device "
      "can put you at risk of cyber crime?\n")

print("IoT - (Internet of Things) which of course is just a fancy term for Wi-Fi enabled appliances - devices have also"
      " created more vulnerabilities because they are connected to the internet.\n")

# Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, and "
      "availability. It is the common model used for finding vulnerabilities and methods for creating "
      "solutions in cybersecurity.")

print("Would you like to learn about the CIA Triad?")
give_info = input("Type 'yes' or 'no'\n")

# Explains pillars of CIA Triad
while give_info.lower() == "yes":
    print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: "
          "\n(a) confidentiality \n(b) integrity \n(c) availability \n(d) none")
    topic = input()

    if topic.lower() == "a":
        print("Confidentiality makes sure data is kept private. Key methods for doing that include keeping levels of "
              "access and setting permissions, encrypting data and files and requiring multi factor authentication.\n")

    elif topic.lower() == "b":
        print("Integrity makes sure that data is reliable, authentic and has not been tampered with. "
              "It is maintained by using version controls that prevent accidental or unauthorized changes "
              "from becoming a problem and using cryptography to securely check for changes.\n")

    elif topic.lower() == "c":
        print("Availability makes sure authorized people can access the data. It means that systems and applications "
              "must be functioning at all necessary times. It can be enhanced by staying on top of upgrades to "
              "software packages and having an effective plan for disaster recovery.\n")

    elif topic.lower() == "d":
        break

    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")

# Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
