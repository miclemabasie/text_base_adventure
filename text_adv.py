# creating a text base adventure game
player_name = input('please enter your name: ')

def intro(name):
    print(f"Hi {name}!! \n Welcome to the text adventure game.")
    print("""in this game you have two rooms to get passe on your way to a safe house, one has a bufferlo in it and the other has a monster you would be given options to choose what to do with each of them at your own risk """)
    print("so without futher ado, let's get started")
    print(f"enjoy the game {player_name}")

def main():
    intro(player_name)
    mkchoice = input("would you like to play anyways? 'YES' or 'NO' ")
    if mkchoice.lower() == 'yes':
        choice = input("choose a door 'r' for right or 'l' for left: ")
        if choice.lower() == 'r':
            monster()
        elif choice.lower() == 'l':
            buffelo() 
    else:
        print("well! good bye then")
    


def buffelo():
    print("you are now in a room with a buffelo")
    print("would you like to get some of his chease or walk away quietly? ")
    choice = input("'yes' get some of his chease or 'no'? ")
    if choice.lower() == 'yes':
        print("Oops you loose mann ")
        print("Game Over")
    elif choice.lower() == 'no':
        print("you are out of the monster's room")
        print("would you like to go to a safe house or may be visit the bufferlo")
        answer = input("'yes' to the safe house or 'no'? ")
        if answer.lower() == 'no':
            monster()
        if answer.lower() == 'yes':
            print("you have successfuly reached the safe house")
        


def monster():
    print("you are now in a room with a monster")
    print("would you like to get some of his chease or walk away quietly? ")
    choice = input("'yes' or 'no'? ")
    if choice.lower() == 'yes':
        print("Oops you loose mann ")
        print("Game Over")
    elif choice.lower() == 'no':
        print("you are out of the monster's room")
        print("would you like to go to a safe house or may be visit the bufferlo")
        answer = input("'yes' to the safe house or 'no'? ")
        if answer.lower() == 'no':
            buffelo()
        if answer.lower() == 'yes':
            print("you have successfuly reached the safe house")
        
    

main()

