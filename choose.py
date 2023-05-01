from deck import *
def choose_card(deck):
  if not deck:
    deck = create_deck()
    reshuffle_count += 1
  return deck.pop()