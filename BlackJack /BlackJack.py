import random
from art import logo

print(logo)

# 2- 10 = Face value cards
# J(Jack), Q(Queen), K(King) = 10
# Ace = 1 or 11
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    while True:
        continue_blackjack = True
    
        # For user
        user_cards = random.sample(cards, 2)
        user_score = sum(user_cards)
        print("\n" * 2)
        print(f"Your cards: {user_cards}, Current score: {user_score}")
        # For computer
        dealer_cards1 = random.choice(cards)
        print(f"Computer's first card: {dealer_cards1}")
        
        while continue_blackjack:
            z = input("Type 'yes/y' to get another card and type 'no/n' to pass: ").lower()
            if z in ['yes', 'y']:
                user_cards = user_cards + [random.choice(cards)]
                user_score = sum(user_cards)
                print(f"Your Final cards: {user_cards}, Final score: {user_score}")

                dealer_cards2 = random.choice(cards)
                dealer_cards = [dealer_cards1, dealer_cards2]
                dealer_score = sum(dealer_cards)
                print(f"Dealer's Final hand: {dealer_cards}, Final score: {dealer_score}")
                
                if user_score > 21:
                    print("You went over\nYou Lose")
                elif dealer_score > 21:
                    print("Dealer went over\nYou Win")
                elif user_score > dealer_score:
                    print("Dealer's Busted\nYou win!")
                elif dealer_score > user_score:
                    print("You're Busted\nDealer wins!")
                continue_blackjack = False
                
            else:
                # User typed 'no', show dealer's cards and result
                print(f"Your Final cards: {user_cards}, Final score: {user_score}")
                
                dealer_cards2 = random.choice(cards)
                dealer_cards = [dealer_cards1, dealer_cards2]
                dealer_score = sum(dealer_cards)
                print(f"Dealer's final hand: {dealer_cards}, Final score: {dealer_score}")
                
                if user_score > 21:
                    print("You went over\nYou Lose")
                elif dealer_score > 21:
                    print("Dealer went over\nYou Win")
                elif user_score > dealer_score:
                    print("Dealer's Busted\nYou win!")
                elif dealer_score > user_score:
                    print("You're Busted\nDealer wins!")
                continue_blackjack = False
        
        print("\n" * 2)
        again = input("Play again? Type 'yes' or 'no': ").lower()
        if again != 'yes':
            print("\n" * 2)
            print("Thank You for playing with us\nWe hope that you had a Great Experience")
            break

blackjack()
