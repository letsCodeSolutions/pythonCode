films ={
    "Finding Dory" :[13,3],
    "Bourne": [13,2],
    "Tarzan": [15,2],
    "Ghost Busters": [18,2]
    }

while True:
    choice = input("Kindly enter the movie name you want to watch ").strip().title()
    if choice in films:
        age = int(input("Enter your age? ").strip())
        if age >= films[choice] [0]:
            if films[choice] [1]>0 :
                enjoy ="Enjoy {}"
                print(enjoy.format(choice))
                films[choice] [1] = films[choice] [1]-1
            else:
                print("Ticket sold out")
        else:
            print("You dont meet the required age criteria")

    else:
        print("We dont hold the movie of your choice")
        
