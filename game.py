from deck import*
from sum import*
from choose import*

def play_game():
  game = input("Would you like to play a game of BlackJack? (yes/no): ").lower()
  while game not in ['yes', 'no']:
    game = input("invalid syntax, Please type either yes or no: ")
  if game == 'no':
    print('GoodBye!')
  score = 1000
  reshuffle_count = 0
  while score > 0 and game == "yes":
    print(f"You have {score} points.")
    bet = input("How much would you like to bet? ")
    try:
      bet = int(bet)
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
    if bet > score:
      print("Your bet is greater than the number of points you currently have.")
      continue
    elif bet< 0:
      print("Invalid input. Please enter a positive number.")
      continue

    deck = create_deck()
    player_cards = [choose_card(deck), choose_card(deck)]
    computer_cards = [choose_card(deck), choose_card(deck)]

    while True:
      sum_player_cards = card_sum(player_cards)
      sum_computer_cards = card_sum(computer_cards)
      print(f"Your cards: {[card['card'] for card in player_cards]}")
      print(f'Your cards total: {sum_player_cards}')
      print(f"Computer Cards: {[card['card'] for card in computer_cards]}")
      print(f'Computer cards total: {sum_computer_cards}')
      choice_hit_stand = input("Do you want to hit or stand? ").lower()
      if choice_hit_stand == "hit":
        player_cards.append(choose_card(deck))
        sum_player_cards = card_sum(player_cards)
        if sum_player_cards > 21:
          print(f"Your cards: {[card['card'] for card in player_cards]}")
          print("You bust! Computer wins!")
          score -= bet
          break
      elif choice_hit_stand == "stand":
        break
      else:
          print("Invalid syntax. Please type 'hit' or 'stand'.")

    if sum_player_cards <= 21:
      while card_sum(computer_cards) < 17:
          computer_cards.append(choose_card(deck))
      sum_computer_cards = card_sum(computer_cards)
      print(f"Computer's cards: {[card['card'] for card in computer_cards]}")
      if sum_computer_cards > 21:
          print("Computer busts! You win!")
          score+= bet
      elif sum_player_cards > sum_computer_cards:
        print("You win!")
        score+= bet
      elif sum_player_cards < sum_computer_cards:
        print("You Lose!")
        score-= bet
      elif sum_player_cards == sum_computer_cards:
        print('tie')
    game = input('Would you like to play again? (yes/no): ').lower()