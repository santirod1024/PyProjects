import random

while True:
    possible_outcomes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    botnum = int(random.choice(possible_outcomes))

    user_choice = int(input("Enter guess: "))
    count = 1

    while user_choice != botnum:

        count += 1

        if user_choice > botnum:
            print("Guess lower: ")
            user_choice = int(input("enter guess: "))

        elif user_choice < botnum:
            print("Guess higher: ")
            user_choice = int(input("enter guess: "))

        if user_choice == botnum:
            print("PSYCHIC ONG")
            print("count- " + str(count))


    if input("Do you wanna play again?(y/n): ") == "y":
        print('''
        
                    ''')
        continue
    else:
            break






