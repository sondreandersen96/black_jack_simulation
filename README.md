# Black Jack Simulation

## What is this program doing? 

This is a Black Jack Simulator, which allows for simulating thousands(or millions) of rounds of the game. Further, the program can store results and compare payoffs and strategies. 


## Explanation of Code
This simulator is build by taking advantage of object oriented programming. The logic of the game being simulated is buildt from the ground up, that is; no Black Jack packages are used. The simulator is based on three objects:

1. Dealer 
1. Player 
1. Deck of cards

The Dealer and Player object are initiated before the program starts to run many simulations, while the deck of cards is initated each time the simulation loop starts over - this effectively pulls all the cards back into the deck and shuffles it. 

**Dealer**

The dealer class is quite simple, it has an instance variable called *hand*, which stores the players hand. And a **hit()** function that incorporates the rules which states that the dealer must hit (take one more card from the deck) if the sum of his cards are lower than 17. This hit function returns true or false. 

```python
class Dealer:
    def __init__(self):
        self.hand = []

    def hit(self):
        score = sum_hand(self.hand)

        # Dealer strategy (based on the rules of the game)
        if score < 17:
            return True
        else:
            return False
```

**Player**

The player class is almost equal to the *dealer* class except that in addition to the instance variable *hand* the player also has and instance variable *balance*. The **hit()** function is a little more complicated for the player, but not much. The main difference is that the player can see one of the dealer's cards, so knowledge about this one card are incorporated into the player strategy. By changing the strategies in this function, users of this program can experiment with different strategies and compare payoffs over time. 

```python
class Player:
    def __init__(self):
        self.hand = []
        self.balance = 10000

    def hit(self, first_dealer_card):
        score = sum_hand(self.hand)

        # Player strategy
        if score == 8:
            return True
        elif first_dealer_card in ['9', '10', '11', '12', '13', 'ace'] and score < 18:
            return True
        elif score < 16:
            return True
        else:
            return False

```

**Deck of cards** 
The deck of cards class deals with all services a deck provides in the game, that is it stores all the card values, it shuffles the deck, and it deals cards to the players. The two functions are almost equal: **deal_cards()** deals the first to cards that are assigned to all players. **one_more_card()** is called when a player chose to *hit*, and it deals one more card, and removes it from the deck. 

```python
class Deck_of_cards:
    def __init__(self):
        self.dec = ['2', '2', '2', '2',
                '3', '3', '3', '3',
                '4', '4', '4', '4',
                '5', '5', '5', '5',
                '6', '6', '6', '6',
                '7', '7', '7', '7',
                '8', '8', '8', '8',
                '9', '9', '9', '9',
                '10', '10', '10', '10',
                '11', '11', '11', '11',
                '12', '12', '12', '12',
                '13', '13', '13', '13',
                'ace', 'ace', 'ace', 'ace']
        shuffle(self.dec)

    # Return two cards, and remove them from the dec
    def deal_cards(self):
        # Pick the two final cards of the deck
        self.two_cards = self.dec[-2:]
        # Remove the two final cards (<= the cards that have been dealt to a player/dealer)
        self.dec.pop()
        self.dec.pop()
        return self.two_cards

    # This function deals one more card to a player.
    def one_more_card(self):
        # Pick the final card of the deck
        self.card = self.dec[-1:]
        # Remove the card that has been delt
        self.dec.pop()
        return self.card
```

All the classes discussed above are stored in the **game_classes_and_functions.py** file. In addition to these classes the file also contain a helper function that sums a hand. The reason a function is required for this seemingly simple operation is that *aces* can both be worth 1 and 11, it is up to the player. The **sum_hand()** function takes care of this, and returns the players score. 


## Game logic 

The game logic is quite simple, and is written in the main.py file. 

First, an instance of the dealer and player is created:
```python
dealer = Dealer()
player = Player()
```

For each round of Black Jack (for each run of the loop) a deck of cards is initiated. Then a hand is dealt to both the player and the dealer:
```python
# Create a new deck of cards
deck_of_cards = Deck_of_cards()

# Deal cards to dealer
dealer.hand = deck_of_cards.deal_cards()

# Deal cards to players
player.hand = deck_of_cards.deal_cards()
```

After the first cards are dealt a **while** loop runs as long as the player or the dealer still want to hit, if one of them chooses to hit a new card is dealt to them. 

```python
# Decide wheter to hit or stand
while player.hit(dealer.hand[0]) == True or dealer.hit() == True:

    if player.hit(dealer.hand[0]):
        player.hand += deck_of_cards.one_more_card()

    if dealer.hit():
        dealer.hand += deck_of_cards.one_more_card()
```

Finally, a winner is chosen based on a bunch of if-else-statements.


## Findings From the Simulations 








