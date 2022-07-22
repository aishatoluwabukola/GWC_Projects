breach_year = 2014

# Greets user
print("Hello! I'm Breach Bot.")
user_name = input("What is your name?\n")
print("Nice to meet you " + user_name)

# Recounts year of breach
todays_year = input("\nWhat year is it?\n")
time_passed = int(todays_year) - breach_year
print("\nWow! That means it has been " + str(time_passed) + " years since Yahoo Data Breach!")

# Introduces breach

print("Would you like to learn about the Yahoo Data Breach 2014?")
give_info = input("Type 'yes' or 'no'\n")

# Explains breach
while give_info.lower() == "yes":
    print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: "
          "\n(a) breach details \n(b) organization's response \n(c) I would like to hear your reflection")
    topic = input()

    if topic.lower() == "a":
        print("\nPersonal information of about 500 million Yahoo users including their email addresses, real names, "
              "phone numbers, dates of birth and passwords were stolen by hackers. Yahoo did not give any further "
              "report about the incident, only claimed that users’ financial account details were secure even though "
              "the stolen emails, password, security questions and answers could give the penetrators access to users'"
              " financial details.")

    elif topic.lower() == "b":
        print("\nYahoo announced the breach, two years after it happened, to its users and advised them to change "
              "their security and accounts’ details. It also reported that the federal agents would be investigating "
              "the incident.")

    elif topic.lower() == "c":
        break

    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")

    input("Press enter to continue\n")

# Introduces my take

print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
give_info = input("Type 'yes' or 'no'\n")

# Shares my take
while give_info.lower() == "yes":
    print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: "
          "\n(a) relation to the CIA Triad \n(b) my reaction \n(c) my advice \n(d) none")
    topic = input()

    if topic.lower() == "a":
        print("\nYahoo did not implement an improved and robust security system and that provided a crack "
              "for hackers to access users’ information.")

    elif topic.lower() == "b":
        print("\nI disagree with the organization's response because Yahoo delayed reporting this breach. "
              "If they had reported earlier, users would have been able to make necessary changes to their accounts’ "
              "details earlier and be more alert. They also should have offered credit monitoring services to the "
              "affected users.\n\nOverall, the breach reflects badly on Yahoo’s proactiveness and security systems. "
              "A breach had occurred earlier in 2013 and they still didn't design a better security system. "
              "It shows that the company has a seemingly lax attitude towards security and probably does not care "
              "about their users’ safety and general well being.")

    elif topic.lower() == "c":
        print("\nI would convince victims to take action by telling them that their personal information could be used"
              " in committing crimes and can also expose them to danger.\n\nMy advice would be to quickly change all "
              "their security details, even on accounts not linked with their Yahoo email. I would also advise them to "
              "keep track of their financial accounts’ transactions, contact the banks they have accounts with to "
              "inform them of possible malicious transactions in the future and also to be more security conscious.")

    elif topic.lower() == "d":
        break

    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")

    input("Press enter to continue\n")

# Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
