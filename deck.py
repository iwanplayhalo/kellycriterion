import random
import matplotlib.pyplot as plt 

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

hand_rankings = { # Hand table taken from reddit :sob:
    # Pairs
    'AA': 0, 'KK': 1, 'QQ': 2, 'JJ': 3, 'TT': 4, '99': 7, '88': 9, '77': 12,
    '66': 16, '55': 20, '44': 23, '33': 33, '22': 22,
    
    # Suited hands
    'AKs': 2, 'AQs': 2, 'AJs': 3, 'ATs': 5, 'A9s': 8, 'A8s': 10, 'A7s': 13,
    'A6s': 14, 'A5s': 12, 'A4s': 14, 'A3s': 14, 'A2s': 17,
    'KQs': 3, 'KJs': 3, 'KTs': 6, 'K9s': 10, 'K8s': 16, 'K7s': 19, 'K6s': 24,
    'K5s': 25, 'K4s': 25, 'K3s': 26, 'K2s': 26,
    'QJs': 5, 'QTs': 6, 'Q9s': 10, 'Q8s': 19, 'Q7s': 26, 'Q6s': 28, 'Q5s': 29,
    'Q4s': 29, 'Q3s': 30, 'Q2s': 31,
    'JTs': 6, 'J9s': 11, 'J8s': 17, 'J7s': 27, 'J6s': 33, 'J5s': 35, 'J4s': 37,
    'J3s': 37, 'J2s': 38,
    'T9s': 10, 'T8s': 16, 'T7s': 25, 'T6s': 31, 'T5s': 40, 'T4s': 40, 'T3s': 41,
    'T2s': 41,
    '98s': 17, '97s': 24, '96s': 29, '95s': 38, '94s': 47, '93s': 47, '92s': 49,
    '87s': 21, '86s': 27, '85s': 33, '84s': 40, '83s': 53, '82s': 54,
    '76s': 25, '75s': 28, '74s': 37, '73s': 45, '72s': 56,
    '65s': 27, '64s': 29, '63s': 38, '62s': 49,
    '54s': 28, '53s': 32, '52s': 39,
    '43s': 36, '42s': 41,
    '32s': 46,
    
    # Offsuit hands
    'AKo': 5, 'AQo': 8, 'AJo': 12, 'ATo': 18, 'A9o': 32, 'A8o': 39, 'A7o': 45,
    'A6o': 51, 'A5o': 44, 'A4o': 46, 'A3o': 49, 'A2o': 54,
    'KQo': 9, 'KJo': 14, 'KTo': 20, 'K9o': 35, 'K8o': 50, 'K7o': 57, 'K6o': 60,
    'K5o': 63, 'K4o': 67, 'K3o': 67, 'K2o': 69,
    'QJo': 11, 'QTo': 15, 'Q9o': 22, 'Q8o': 36, 'Q7o': 53, 'Q6o': 66, 'Q5o': 71,
    'Q4o': 75, 'Q3o': 76, 'Q2o': 77,
    'JTo': 21, 'J9o': 34, 'J8o': 48, 'J7o': 64, 'J6o': 80, 'J5o': 74, 'J4o': 82,
    'J3o': 85, 'J2o': 86,
    'T9o': 31, 'T8o': 43, 'T7o': 59, 'T6o': 74, 'T5o': 89, 'T4o': 90, 'T3o': 92,
    'T2o': 94,
    '98o': 42, '97o': 55, '96o': 68, '95o': 83, '94o': 95, '93o': 96, '92o': 97,
    '87o': 52, '86o': 61, '85o': 73, '84o': 88, '83o': 98, '82o': 99,
    '76o': 57, '75o': 65, '74o': 78, '73o': 93, '72o': 100,
    '65o': 58, '64o': 70, '63o': 81, '62o': 95,
    '54o': 62, '53o': 72, '52o': 84,
    '43o': 76, '42o': 86,
    '32o': 91,
}

def normalize_hand(card1, card2):
    # Convert two cards (as integers 0-51) into standard hand notation.

    rank1 = Deck.rank(card1)
    rank2 = Deck.rank(card2)
    suit1 = Deck.suit(card1)
    suit2 = Deck.suit(card2)
    
    ranks = "23456789TJQKA"
    
    # Order by rank 
    if rank1 < rank2:
        rank1, rank2 = rank2, rank1
        suit1, suit2 = suit2, suit1
    
    rank1_char = ranks[rank1]
    rank2_char = ranks[rank2]
    
    # Check if suited
    if suit1 == suit2:
        if rank1 == rank2:
            return rank1_char + rank2_char  # Pair
        else:
            return rank1_char + rank2_char + 's'  # Suited
    else:
        if rank1 == rank2:
            return rank1_char + rank2_char  # Pair
        else:
            return rank1_char + rank2_char + 'o'  # Offsuit

def get_hand_rank(card1, card2):
    # Get the ranking (0-100) for a two-card hand.
    hand = normalize_hand(card1, card2)
    return hand_rankings.get(hand, 100)

def hand_percentile(card1, card2):
    # Convert hand rank to percentile (0.0 = worst, 1.0 = best).
    rank = get_hand_rank(card1, card2)
    # Normalize to 0-1 (100 is worst, 0 is best)
    percentile = 1 - (rank / 100)
    return percentile

def villain_play(hand, aggression): # make a tunable aggression parameter based off of how we want our villain to act based off of their hand strength
    percentile = hand_percentile(hand[0], hand[1])
    rank = get_hand_rank(hand[0], hand[1])

    if percentile > aggression: 
        if random.random() < 0.85:  # mostly raise
            size = 2.5 + random.uniform(-0.5, 0.5)  # 2-3 big blind 
            return {'action': 'raise', 'size': size, 'percentile': percentile, 'rank': rank}
        else:  # sometimes just call
            return {'action': 'call', 'size': 1.0, 'percentile': percentile, 'rank': rank}
    else:
        # Hand not good enough - fold pr bluff
        if random.random() < 0.05:  # bluff
            size = 2.5 + random.uniform(0, 1.0)
            return {'action': 'raise', 'size': size, 'percentile': percentile, 'rank': rank}
        else: # fold
            return {'action': 'fold', 'size': 0, 'percentile': percentile, 'rank': rank}
        
class Poker: 
    def __init__(self, bigblind = 10, aggression=0.5, starting_stack = 1000, ante_rate = 0.1):
        self.deck = Deck()
        self.stack = starting_stack
        self.bigblind = bigblind
        self.aggression = aggression
        self.ante_rate = ante_rate
        self.history = []
    
    def play_hand(self):
        # added ante to create pressure. without pressure it's never busting 
        ante = self.bigblind * self.ante_rate
        self.stack -= ante
        
        if self.stack <= 0:
            return -ante
        
        # start
        deck = Deck()
        player_hand = deck.deal(2)
        villain_hand = deck.deal(2)
        villain_action = villain_play(villain_hand, self.aggression)
        if villain_action['action'] == 'fold':
            profit = 1.5 * self.bigblind # win 
            self.stack += profit
            self.history.append({
                'player_hand': player_hand,
                'villain_hand': villain_hand,
                'villain_action': villain_action,
                'result': 'villain_folded',
                'profit': profit
            })
            return profit
        pot = 3.5 * self.bigblind + (villain_action['size'] - 1) * self.bigblind
        call_amount = villain_action['size'] * self.bigblind

        # estimate 
        your_percentile = hand_percentile(player_hand[0], player_hand[1])
        villain_percentile = villain_action['percentile']

        if your_percentile > villain_percentile:
            equity = 0.65 
        elif your_percentile < villain_percentile:
            equity = 1-0.65
        else:
            equity = 0.5

        # decision
        kelly_f = 2 * equity - 1
        max_kelly = kelly_f * self.stack if kelly_f > 0 else 0
        ev = equity * (pot + call_amount) - (1 - equity) * call_amount
        should_call = call_amount <= max_kelly and ev > 0

        # playing it out
        if should_call:
            if random.random() < equity:
                profit = pot
                self.stack += profit
                result = 'won'
            else:
                profit = -call_amount
                self.stack -= call_amount
                result = 'lost'
        else:
            profit = profit = -self.bigblind
            self.stack -= self.bigblind
            result = 'folded'

        self.history.append({
            'player_hand': player_hand,
            'villain_hand': villain_hand,
            'villain_action': villain_action,
            'result': result,
            'profit': profit,
            'equity': equity
        })
        return profit 

def run_simulation(nums_hands = 1000, starting_stack = 1000, bigblind = 10, aggression = 0.5):
    game = Poker(starting_stack = starting_stack, bigblind = bigblind, aggression = aggression)
    stack_history = [starting_stack]

    for i in range(num_hands):
        game.play_hand()
        stack_history.append(game.stack)

        if game.stack <= 0:
            break # no moni
    
    return stack_history

num_simulations = 100
num_hands = 500
all_paths = []

for i in range(num_simulations):
    path = run_simulation(nums_hands = num_hands, starting_stack = 1000, bigblind = 10, aggression = 0.5)
    all_paths.append(path)
    print(f"Simulation {i+1}: Final stack = {path[-1]:.2f}")

for path in all_paths:
    plt.plot(path, alpha = 0.3)

plt.axhline(1000, color='red', linestyle='--', alpha=0.5, label='Starting stack')
plt.yscale('log')
plt.xlabel('Hand Number')
plt.ylabel('Stack Size ($)')
plt.title(f'Kelly Criterion Poker Simulation ({num_simulations} paths)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Statistics
final_stacks = [path[-1] for path in all_paths]
print(f"\n=== RESULTS ===")
print(f"Mean final stack: ${sum(final_stacks)/len(final_stacks):.2f}")
print(f"Median final stack: ${sorted(final_stacks)[len(final_stacks)//2]:.2f}")
print(f"Bust rate: {sum(1 for s in final_stacks if s <= 0)/len(final_stacks)*100:.1f}%")
print(f"Profitable: {sum(1 for s in final_stacks if s > 1000)/len(final_stacks)*100:.1f}%")