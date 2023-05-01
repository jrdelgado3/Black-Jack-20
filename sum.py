def card_sum(cards):
  card_sum = sum(card["value"] for card in cards)
  for card in cards:
    if card["value"] == 11 and card_sum > 21:
        card_sum -= 10
  return card_sum