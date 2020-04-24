# Start the game
import random

print("Welcome to C859 - Python Experience Lab - Blackjack – Starter webinar")

delaerCards = []

playerCards = []

# Dealer: Deal the cards; how to deal first two cards?
while (len(delaerCards) != 2):
    delaerCards.append(random.randint(1, 11))  # 1 to 11 are card values

# Player: Deal the cards; how to deal first two cards?
while (len(playerCards) != 2):
    playerCards.append(random.randint(1, 11))  # 1 to 11 are card values

# Display the cards
print("Dealer cards: " + str(delaerCards))
print("Player cards: " + str(playerCards))

# Sum of Dealer cards
dcSum = sum(delaerCards)
print("Dealer cards sum: " + str(dcSum))

# Sum of Player cards
pcSum = sum(playerCards)
print("Player cards sum: " + str(pcSum))

# Compare the sum of the cards between Dealer vs. Player
# pcSum=21 # to test
if pcSum == 21 and dcSum == 21:
    print("Tie !!!")
elif pcSum > 21:
    print("Bust. Player lost!")
elif dcSum > 21:
    print("Bust. Dealer lost!")
elif pcSum == 21 and dcSum < 21:
    print("Player won!")
elif pcSum < 21 and dcSum == 21:
    print("Dealer won!")
else:  # pcSum < 21 and dcSum < 21 and (pcSum maybe < or > dcSum)
    print("Option to Player: Hit or Stand")
    # Option to Player: Hit or Stand until pcSum >= 21
    while (pcSum < 21):
        try:
            pChoice = input("Choose your option, type: Hit or Stand: ")
            if pChoice.lower() == 'hit':  # Hit
                playerCards.append(random.randint(1, 11))
                print("Player cards: " + str(playerCards))
                pcSum = sum(playerCards)
                print("Player cards sum: " + str(pcSum))
                
                # check player hand 
                if pcSum == 21:
                    print("Yay! Player won!")
                    break
                elif pcSum > 21:
                    print("Bust. Player lost!")
                    break
            # else:
            #     continue  # not really needed in this case; why?
            elif pChoice.lower() == 'stand':  # Stand;
    #
                # !!! COMPLETE THE CODE !!! Deal Dealer's hand until Dealer reaches 17
                #
                while (dcSum < 18):
                    delaerCards.append(random.randint(1, 11))
                    print("Dealer cards: " + str(delaerCards))
                    dcSum = sum(delaerCards)
                    print("Dealer cards sum: " + str(dcSum))
                
                print("Player cards: " + str(playerCards))
                pcSum = sum(playerCards)
                print("Player cards sum: " + str(pcSum))
                print("Dealer cards: " + str(delaerCards))
                dcSum = sum(delaerCards)
                print("Dealer cards sum: " + str(dcSum))
                # check dealer hand and compare
                # !!! COMPLETE THE CODE !!! what happens if dcSum=21 or dcSum>21
                #
                #if (...)
                #  print(...)
                #elif (...)
                #  print(...)
                # ??
                if dcSum == 21:
                    print("Dealer wins...")
                    break
                elif dcSum > 21:
                    print("Bust. Dealer lost!")
                    break


                if pcSum > dcSum:
                    print("Player won!")
                else:
                    print("Delear won!")  # pcSum <= dcSum:
                break # exit loop
            else:
                print('Invalid option selected.')
        except ValueError as excpt:
            print(excpt)
            print('Invalid option selected. Exiting game...\n')