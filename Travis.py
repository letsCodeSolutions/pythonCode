known_users = ["Rakesh","Rohan","Sita","Laxman","Son"]
print(known_users)

while True:
    print("Hi my name is Travis")
    name = input("What is your name: ").strip().capitalize()
    if name in known_users:
        print("Hello {} ".format(name))
        remove = input("Would you like to be removed from the list? (y/n)").strip().lower()
        if remove == 'y':
            known_users.remove(name)
            print(known_users)
        elif remove == 'n':
            print("I would not like you to leave the list")
    else:
        print("Hi {}, I think I have not met you yet ".format(name))
        add_user = input("Would you like to join the list? (y/n)").strip().lower()
        if add_user == 'y':
            known_users.append(name)
            print(known_users)
        elif add_user == 'n':
            print ("See you soon then!")
        
        
    
    
