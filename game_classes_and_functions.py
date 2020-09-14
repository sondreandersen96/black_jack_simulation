from random import shuffle


card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    '11': 10,
    '12': 10,
    '13': 10,
    'ace': [1, 11]
}


# This function sums the players hand, and decides whether ace is one or
def sum_hand(hand):
    score = 0

    # If the hand does not contain any aces, the sum is easially computed
    if 'ace' not in hand:
        for card in hand:
            score += card_values[card]
    else:
        # Sum ace = 11
        score_ace_11 = 0
        for card in hand:
            if card == 'ace':
                score_ace_11 += 11
            else:
                score_ace_11 += card_values[card]

        # Sum ace = 1
        score_ace_1 = 0
        for card in hand:
            if card == 'ace':
                score_ace_1 += 1
            else:
                score_ace_1 += card_values[card]
        # Compare

        if score_ace_11 <= 21 and score_ace_11 > score_ace_1:
            score = score_ace_11
        else:
            score = score_ace_1

    return score



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
