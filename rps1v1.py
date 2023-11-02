while True:

    print("Rock")
    print("Paper")
    print("Scissors")

    user_outcome = input("Shoot! Make selection: ")
    print('''
    
    
    
    
    
    
    ''')

    print("Rock")
    print("Paper")
    print("Scissors")

    computer_outcome = input("Shoot! Make a selection: ")

    if user_outcome == computer_outcome:
        print("Tie Game, Try Again")

    elif user_outcome == "rock":
        if computer_outcome == "scissors":
            print("Player 1 Wins")
        elif computer_outcome == "paper":
            print("Player 2 Wins")
        elif computer_outcome == "rock":
            print("Tie Game, Try Again")


    elif user_outcome == "paper":
        if computer_outcome == "scissors":
            print("Player 2 Wins")
        elif computer_outcome == "rock":
            print("PLayer 1 Wins")
        elif computer_outcome == "paper":
            print ("Tie Game. Try Again")



    elif user_outcome == "scissors":
        if computer_outcome == "rock":
            print("Player 2 Wins")
        elif computer_outcome == "paper":
            print("PLayer 1 wins")
        elif computer_outcome == "scissors":
            print("Tie Game, Try Again")

    else:
        print("invalid selection")

    print('''
    
    ''')
    if input("Do you wanna play again?(y/n): ") == "y":
        print('''
        
        ''')
        continue
    else:
        break