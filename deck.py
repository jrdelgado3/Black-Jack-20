import random
CARD_VALUES = {
  "Ace": 11,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "Jack": 10,
  "Queen": 10,
  "King": 10,
}
def create_deck():
  deck = []
  for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
    for value in CARD_VALUES:
      deck.append({"card": f"{value} of {suit}", "value": CARD_VALUES[value]})
  random.shuffle(deck)
  return deck