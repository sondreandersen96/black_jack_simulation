'''
This program is a black jack simulator.

It be expanded to test different strategies, and compare results.

For now, splits are not allowed.

The strategy of the player is quite simple.

The game is based on the player being able to see one
of the dealers cards, both not both.

The dealer must hit if his score is lower than 17. And
must stand otherwise.

'''

from game_classes_and_functions import sum_hand, Deck_of_cards, Dealer, Player

from random import shuffle
from matplotlib import pyplot as plt
import pandas as pd


# Opening or creating a dataframe to store historic results
try:
    df = pd.read_csv('historic_bets.csv')
except:
    df = pd.DataFrame({})



# Declare an instance of the dealer and player before the game starts
dealer = Dealer()
player = Player()

# The player bets this amount each round
bet = 50




# This is one player
results = []
balances = [player.balance]

# Test round
for i in range(800):

    # Create a new deck of cards
    deck_of_cards = Deck_of_cards()

    # Deal cards to dealer
    dealer.hand = deck_of_cards.deal_cards()

    # Deal cards to players
    player.hand = deck_of_cards.deal_cards()

    #print('Player hand:', player.hand, 'Player score:', sum_hand(player.hand))
    #print('Dealer hand:', dealer.hand, 'Dealer score:', sum_hand(dealer.hand))


    # Decide wheter to hit or stand
    while player.hit(dealer.hand[0]) == True or dealer.hit() == True:

        #print('player', player.hit(dealer.hand[0]))
        #print('dealer', dealer.hit())


        if player.hit(dealer.hand[0]):
            player.hand += deck_of_cards.one_more_card()

            #print('Player - HIT', player.hand, sum_hand(player.hand))

        if dealer.hit():
            dealer.hand += deck_of_cards.one_more_card()

            #print('Dealer - HIT', dealer.hand, sum_hand(dealer.hand))



    # Compare score and declare a WINNER
    winner = 0
    player_score = sum_hand(player.hand)
    dealer_score = sum_hand(dealer.hand)

    #print('\n'*10)
    #print('Player hand:', player.hand, ' Player score:', sum_hand(player.hand))
    #print('Dealer hand:', dealer.hand, ' Dealer score:', sum_hand(dealer.hand))


    if player_score == 21 and dealer_score != 21:
        winner = 'player'
    elif dealer_score == 21 and player_score != 21:
        winner = 'dealer'
    elif player_score == dealer_score:
        winner = 'tie'
    elif player_score > dealer_score and player_score < 21:
        winner = 'player'
    elif dealer_score > player_score and dealer_score < 21:
        winner = 'dealer'
    elif dealer_score > 21 and player_score <= 21:
        winner = 'player'
    elif player_score > 21 and dealer_score <= 21:
        winner = 'dealer'
    elif player_score > 21 and player_score > 21:
        winner = 'dealer'
    else:
        winner = 'GAME LOGIC IS OFF!!!!!!!!'

    # Store result from this round
    results.append(winner)

    # Controll the players balance
    if winner == 'player':
        player.balance += bet
    elif winner == 'tie':
        player.balance += 0
    elif winner == 'dealer':
        player.balance -= bet


    # Store the players balance at the end of each round, to
    # ... track development over time.
    balances.append(player.balance)



player_wins = results.count('player')
dealer_wins = results.count('dealer')
ties = results.count('tie')

print(f'Player wins: {player_wins}')
print(f'Dealer wins: {dealer_wins}')
print(f'Ties: {ties}')



plt.hist(results)
plt.show()

plt.plot(balances)
plt.show()



# Save data from this simulation to csv file
player_nr = len(df.columns)

df[player_nr] = balances


df.to_csv('historic_bets.csv', index=False)














#
