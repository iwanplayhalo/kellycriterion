import random
class Deck:
    def __init__(self):
        self.cards = list(range(52))
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, n=1):
        dealt_cards = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt_cards

    def card_name(card):
        ranks = "23456789TJQKA"
        suits = "♥♦♣♠"
        return ranks[Deck.rank(card)] + suits[Deck.suit(card)]
    
    def rank(card):
        return card % 13
    
    def suit(card):
        return card // 13
    