import random

# Define card values
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Deck of cards
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

# Function to calculate the hand value
def calculate_hand_value(hand):
    value = sum(CARD_VALUES[card] for card in hand)
    aces = hand.count('A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Function to deal a card
def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

# Function to display the hand
def display_hand(hand):
    return ', '.join(hand)

# Function to check if the player wants to split
def check_split(player_hand, points):
    if player_hand[0] == player_hand[1] and points >= bet:
        while True:
            choice = input("You have a pair. Do you want to split? (yes/no): ").lower()
            if choice in ['yes', 'no']:
                return choice == 'yes'
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Function to check if the player wants to double
def check_double(points, bet):
    if points >= bet*2:
        while True:
            choice = input("Do you want to double down? (yes/no): ").lower()
            if choice in ['yes', 'no']:
                return choice == 'yes'
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Function to play a single hand
def play_hand(deck, points, bet):
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    print(f"Your hand: {display_hand(player_hand)}")
    print(f"Dealer's hand: {dealer_hand[0]}, ?")
    
    if check_split(player_hand, points):
        return play_split(deck, points, bet, player_hand, dealer_hand)
    
    if check_double(points, bet):
        bet *= 2
        player_hand.append(deal_card(deck))
        print(f"Your hand: {display_hand(player_hand)}")
        if calculate_hand_value(player_hand) > 21:
            print("You bust! You lose.")
            return points - bet
    
    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to 'hit' or 'stand'?: ").lower()
        if action == 'stand':
            break
        elif action == 'hit':
            player_hand.append(deal_card(deck))
            print(f"Your hand: {display_hand(player_hand)}")
            if calculate_hand_value(player_hand) > 21:
                print("You bust! You lose.")
                return points - bet

    print(f"Dealer's hand: {display_hand(dealer_hand)}")
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        print(f"Dealer's hand: {display_hand(dealer_hand)}")
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
        return points + bet
    elif player_value < dealer_value:
        print("You lose.")
        return points - bet
    else:
        print("It's a tie!")
        return points

# Function to handle split
def play_split(deck, points, bet, player_hand, dealer_hand):
    hand1 = [player_hand[0], deal_card(deck)]
    hand2 = [player_hand[1], deal_card(deck)]
    
    print(f"Playing first hand: {display_hand(hand1)}")
    points = play_hand(deck, points, bet)
    
    print(f"Playing second hand: {display_hand(hand2)}")
    points = play_hand(deck, points, bet)
    
    return points

# Main game loop
def play_blackjack():
    points = 2000
    while points > 0:
        print(f"\nYou have {points} points.")
        try:
            bet = int(input("Enter your bet: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if bet > points or bet <= 0:
            print("Invalid bet. Please enter a value within your points.")
            continue

        points = play_hand(deck.copy(), points, bet)

        if points <= 0:
            print("You're out of points! Game over.")
            break
        
        continue_game = input("Do you want to play another round? (yes/no): ").lower()
        if continue_game != 'yes':
            print("Thanks for playing! You finished with", points, "points.")
            break

if __name__ == "__main__":
    play_blackjack()
