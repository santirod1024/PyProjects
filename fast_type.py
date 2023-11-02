import random
import time

#Quote bank
bars = [
    "May the Force be with you. - Star Wars",
    "To be, or not to be: that is the question. - Hamlet",
    "I'll be back. - The Terminator",
    "There's no place like home. - The Wizard of Oz",
    "Elementary, my dear Watson. - Sherlock Holmes",
    "Life is like a box of chocolates; you never know what you're gonna get. - Forrest Gump",
    "Here's looking at you, kid. - Casablanca",
    "You can't handle the truth! - A Few Good Men",
    "I am serious...and don't call me Shirley. - Airplane!",
    "I am not a number, I am a free man! - The Prisoner",
    "You shall not pass! - The Lord of the Rings",
    "All work and no play makes Jack a dull boy. - The Shining",
    "Houston, we have a problem. - Apollo 13",
    "Here's Johnny! - The Shining",
    "I'll have what she's having. - When Harry Met Sally",
    "As God is my witness, I'll never be hungry again. - Gone with the Wind",
    "Keep your friends close, but your enemies closer. - The Godfather Part II",
    "Every man dies, not every man really lives. - Braveheart",
    "What we do in life echoes in eternity. - Gladiator",
    "I am your father. - Star Wars: The Empire Strikes Back",

]

quote = random.choice(bars)#Choose a random quote from the list

# Explain / ready
print("\nWrite the following exactly as you see it as quickly as you can.")
ready = input("Ready? \n")
start_time = int(time.time()*100)
correct = False

#Game 1
while correct == False:
    print(quote)
    answer = input("Type here: ")

    if quote == answer:
        print("\nYou are correct!\n")
        correct = True
    else:
        print("\n\nTry again")

#Player 1 score
end_time = int(time.time()*100)
duration1 = (end_time - start_time)/ 100
words_per_minute = round(len(quote.split()) / duration1 * 60, 2)

print("Your time:  " + str(duration1) + " seconds")
print("Words per minute: " + str(words_per_minute) + "\n\n")

input("When ready press enter and pass to player 2\n\n\n\n\n")

#Player 2 game
print("\n\n\n\n\n\n\nWrite the following exactly as you see it as quickly as you can.")
ready = input("Ready? \n")
start_time2 = int(time.time()*100)
correct = False

while correct == False:
    print(quote)
    answer = input("\nType here: \n")

    if quote == answer:
        print("You are correct!\n")
        correct = True
    else:
        print("\n\nTry again")

#Player 2 score
end_time2 = int(time.time()*100)
duration2 = (end_time2 - start_time2)/ 100
words_per_minute2 = round(len(quote.split()) / duration2 * 60, 2)

print("Your time:  " + str(duration2) + " seconds")
print("Words per minute: " + str(words_per_minute2))

input("\n\nPress enter for results\n\n")

#Declaring winner and printing their time
if duration1 < duration2:
    print("Player 1 Wins!")
    print("\nPlayer 1 time: " + str(duration1))
    print("Player 2 time: " + str(duration2))
elif duration2 < duration1:
    print("Player 2 Wins!")
    print("\nPlayer 2 time: " + str(duration2))
    print("Player 1 time: " + str(duration1))