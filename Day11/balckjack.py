import random


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
random.shuffle(deck)
player__hand = [random.choice(deck), random.choice(deck)]
dealer_hand = [random.choice(deck), random.choice(deck)]
print(f"Your hand: {player__hand}, Dealer's hand: {dealer_hand[0]}")

def calculate_hand_value(hand):
    value = sum(hand)
    if value > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        value = sum(hand)
    return value

def blackjack(player_hand, dealer_hand):
    while True:
        player_value = calculate_hand_value(player_hand)
        print(f"Current value: {player_value}")
        print(f"Dealer's visible card: {dealer_hand[0]}")
        draw_more = input("Do you want to draw another card? (y/n): ").lower()
        if player_value > 21:
            print("You busted! Dealer Wins!")
            return
        if draw_more == 'y':
            player_hand.append(random.choice(deck))
        else: 
            break

    print(f"Your final hand: {player_hand}")
    dealer_value = calculate_hand_value(dealer_hand)
    while dealer_value < 17:
        dealer_hand.append(random.choice(deck))
        dealer_value = calculate_hand_value(dealer_hand)
    
    

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    print(f"Dealer's final hand: {dealer_hand}, Dealer's value: {dealer_value}")

    if player_value == 21 and dealer_value == 21:
        print("Both you and the dealer have BLACKJACK! It's a tie!")
    elif player_value == 21:
        print("BLACKJACK! You Win!")
    elif dealer_value == 21:
        print("Dealer BLACKJACK! Dealer Wins!")
    elif dealer_value > 21:
        print("Dealer busted! You Win!")
    elif player_value > dealer_value:
        print("You Win!")
    elif player_value < dealer_value:
        print("Dealer Wins!")
    else:
        print("It's a tie!")

blackjack(player__hand, dealer_hand)
    