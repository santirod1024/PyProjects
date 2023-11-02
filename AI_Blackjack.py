import random

# define card values
card_values = {
    'Ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

# create deck of cards
deck = list(card_values.keys()) * 4

# function to draw card from deck
def draw_card(deck):
    return deck.pop(random.randint(0, len(deck)-1))

# function to calculate hand value
def hand_value(hand):
    value = sum([card_values[card] for card in hand])
    if 'Ace' in hand and value + 10 <= 21:
        value += 10
    return value

# play blackjack
print("Let's play blackjack!\n")
player_hand = [draw_card(deck), draw_card(deck)]
dealer_hand = [draw_card(deck)]

while True:
    print("Player hand:", player_hand, "Value:", hand_value(player_hand))
    print("Dealer hand:", [dealer_hand[0], '???'])
    action = input("Do you want to hit or stand? ")
    if action.lower() == 'hit':
        player_hand.append(draw_card(deck))
        if hand_value(player_hand) > 21:
            print("Bust! You lose.")
            break
    elif action.lower() == 'stand':
        dealer_hand.append(draw_card(deck))
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(draw_card(deck))
        print("Dealer hand:", dealer_hand, "Value:", hand_value(dealer_hand))
        if hand_value(dealer_hand) > 21:
            print("Dealer bust! You win.")
            break
        elif hand_value(player_hand) > hand_value(dealer_hand):
            print("You win!")
            break
        elif hand_value(player_hand) == hand_value(dealer_hand):
            print("Push.")
            break
        else:
            print("You lose.")
            break
