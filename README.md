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
