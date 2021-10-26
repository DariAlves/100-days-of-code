import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

random.shuffle(cards)

dealer_cards = []
player_cards = []

def random_card():
    card = random.choice(cards)
    return card

for _ in range(2):
    player_cards.append(random_card())
    dealer_cards.append(random_card())

def score_cards(cards):
    """Retorna o valor total do array de cards"""
    total_score = sum(cards)
    if 11 in cards and total_score > 21:
        total_score -= 10
    return total_score

print(player_cards)
print(dealer_cards)

print(score_cards(player_cards))
print(score_cards(dealer_cards))

if score_cards(player_cards) == 21 and score_cards(dealer_cards) == 21:
    print("Draw game!")

if score_cards(player_cards) == 21:
    print("Player wins")

if score_cards(dealer_cards) == 21:
    print("You lose! Dealer wins")
