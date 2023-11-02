import random
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the Pygame window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the Pygame window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the title of the window
pygame.display.set_caption("GREED Window")

#player score and saved score box
user1total = 0
user2total = 0
saved1 = 0
saved2 = 0
winner = False

print("\nThis is GREED\n")
print("This is a die game where you want to be the first to 100 ")
print("Land on a 1 and your bankrupt")
print("You can save your score at any point and cannot fall below that score")
input("\n\nPlayer 1 ready?")

while True:
    while winner is False:
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if user1total < 100:
            userchoice = input("\nRoll or Stay(r/s): \n")
            dicenum = [1, 2, 3, 4, 5, 6]
            diceroll = random.choice(dicenum)
            if userchoice == "r":
                if diceroll == 1:
                    print("\nBankrupt!\n")
                    user1total = saved1
                    print(user1total)
                    print("\nPlayer 2 turn!")
                    print()
                    print("Player 2 score: " + str(saved2))
                    break
                else:
                    print("You rolled a " + str(diceroll))
                    user1total += diceroll
                    print("\nCurrent score: " + str(user1total))
            elif userchoice == "s":
                print("Your saved score is " + str(user1total))
                print()
                print("Player 2 turn!")
                print("Player 2 score: " + str(saved2))
                print()
                saved1 = user1total + 0
                break
        elif user1total >= 100:
            print("Player 1 Won")
            winner = True
            break

    while winner is False:
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if user2total < 100:
            userchoice = input("\nRoll or Stay (r/s): \n")
            dicenum = [1, 2, 3, 4, 5, 6]
            diceroll = random.choice(dicenum)
            if userchoice == "r":
                if diceroll == 1:
                    print("\nBankrupt\n")
                    user2total = saved2
                    print(user2total)
                    print()
                    print("Player 1 turn!")
                    print("Player 1 score: " + str(saved1))
                    print()
                    break
                else:
                    print("you rolled a " + str(diceroll))
                    user2total += diceroll
                    print("Current score: " + str(user2total))

            elif userchoice == "s":
                print("Your saved score is " + str(user2total))
                print()
                print("Player 1 turn!")
                print("Player 1 score: " + str(saved1))
                print()
                saved2 = user2total + 0
                break
        elif user2total >= 100:
            print("Player 2 Won")
            winner = True
            break

