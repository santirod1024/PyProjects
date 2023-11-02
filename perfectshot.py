import random


# Assigning teams
players = []
playernum = int(input("How many players: "))

while len(players) < playernum:
    player = input("Enter name: ")
    players.append(player)

random.shuffle(players)
midpoint = len(players) //2
team1 = players[:midpoint]
team2 = players[midpoint:]

print(f"Team 1: {', '.join(team1)}")
print(f"Team 2: {', '.join(team2)}")
#


# Prompting
category = ["Horror", "Sports", "Drama", "Superhero", "News", "Comedy", "Memes", "Scifi", "Historical",
            "Fantasy", "Mystery", "Romance", "Vintage"]

condition = ["Tripod", "Selfie", "In air", "Animal", "Nature", "Human Structure", "Riding airplane",
            "Monochrome", "Silhouette"]

action = ["Walking Dog", "Tourism", "Crime", "Dueling", "Fighting", "Frightened", "Cooking", "Laughing",
          "Crying", "Dancing", "Exercising", "Vacationing"]

rancat = random.choice(category)
rancon = random.choice(condition)
ranact = random.choice(action)

print(', '.join([rancat, rancon, ranact]))


#scores will be given based on creativity, condition, quality


