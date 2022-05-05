# Python_project_Travis_the_rediculous_security_system

# list of known users

known_users = ['Alice','Bob','Claire','Dan','Emma','Fred','Georgie','Harry']

print(len(known_users)) # length of elements

while True:
    print("Hi! My name is Travis")
    name = input("What is your name? \n").strip().capitalize()
    
    if name in known_users:
        print("Hello {}".format(name))
        remove = input("Would you like to be removed from the system?(Yes/No) \n")

        if remove == 'Yes':
            known_users.remove(name)
            print("Thankyou! Bye! See you next time")
        elif remove == 'No':
            print("I am glad to see you continue.")
        
    else:
        print("Name not recognised")
        add = input("Should I add your name to the system? (Yes/No) \n")
        if add =="Yes":
            known_users.append(name)
            print("Known_users are {}.".format(known_users))
        elif add == 'No':
            print("No worries. See you around.")
    
