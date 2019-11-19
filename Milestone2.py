## Milestone Project 2 - BlackJack Player Game
# Step1: Create a deck of 52 cards
import random
suits = ['Hearts','Diamonds','Spades','Clubs']
ranks = ['one','two','three','four','five','six','seven','eight','nine','ten','king','queen','jack','ace']
values = {'ace':11,'king':10,'queen':10,'jack':10,'ten':10,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
isPlaying = True

# Step2: Create classes for decks and hands
# Card class
class card():
    """docstring for card."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank =  rank
    def __str__(self):
    return self.rank + '' + 'of' + '' + self.suit

# Deck class
class deck(object):
    """docstring for deck."""
    def __init__(self, arg):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def dealCards(self):
        card_dealt = self.deck.pop(0)
        return card_dealt

    def __str__(self):
        return self.deck

# Hand class creation
class hand():
    def __init__(self):
        self.cards = []
        self.card_value = 0
        self.ace_value = 0

    def add_cards(self,card):
        self.cards.append(card)
        self.card_value += card_value[card.ranks]
        if card.rank == 'Ace':
            self.ace_value += 1

    def ace_adjustment(self):
        while self.card_value>21 and self.ace_value:
            self.card_value -=10
            self.ace_value -=1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_betI(self):
        self.total -= self.bet

# Functions for building the game structure
## Place bets

    def take_bet(chips):
        while True:
            try:
                chips.bet = int(input('Enter your betting chips: '))
            except:
                print('Invalid Value!')
            else:
                if chips.bet>chips.total:
                    print('Insufficient number of chips!')
                else:
                    break

    def hit(deck,hand):
        hand.add_card(deck.dealCards())
        hand.ace_adjustment()

    def hit_or_stand(deck,hand):
        global isPlaying

        while True:
            status = input("Enter your choice 'h' or 's'")
            if status[0].lower()=='h':
                hit(deck,hand)
            elif x[0].lower()=='s':
                print('Player stands. Dealer plays')
                isPlaying=False
            else:
                print('Try again!')
                continue
            break

    def show_allCards(player,dealer):
        print('Dealers hand: ',*dealer.cards,sep='\\n')
        print('Dealers hand: ',dealer.value)
        print('Player hand: ',*player.cards,sep='\\n')
        print('Player hand: ',player.value)

# Game situations
    def player_busts(player,dealer,chips):
        print('Player busts!')
        chips.lose_bet

    def player_wins(player,dealer,chips):
        print('Player Wins!')
        chips.win_bet()

    # Dealer busts = player wins

    def dealer_busts(player,dealer,chips):
        print('Dealer Busts')
        chips.win_bet()

    def dealer_wins(player,dealer,chips):
        print('Dealer wins!')
        chips.lose_bet()

    def push(player,dealer):
        print('Player-dealer tie! Its a push')

    # Main Code
    while True:
        print('Welcome to Blackjack')

        # Create and shuffle deck - give 2 cards to each dealer and player
        deck = Deck()
        deck.shuffle()

        player_hand = hand()
        player_hand.add_cards(deck.dealCards())
        player_hand.add_cards(deck.dealCards())

        dealer_hand = hand()
        dealer_hand.add_cards(deck.dealCards())
        dealer_hand.add_cards(deck.dealCards())

        # Player chips
        player_chips = chips() # Start with 100

        # Ask player to place bet
        take_bet(player_chips)

        # Show player cards
        show_allCards(player_hand,dealer_hand)

        while isPlaying:
            # Ask player to hit or stand
            hit_or_stand(deck,player_hand)
            show_allCards(player_hand,dealer_hand)

            if player_hand.value>21:
                player_busts(player_hand,dealer_hand,chips)
                break

            elif player_hand.value<=21:
                while dealer_hand.value < 17:
                    hit(deck,dealer_hand)

                show_allCards(player_hand,dealer_hand)

                if dealer_hand.value>21:
                    dealer_busts(player_hand,dealer_hand,player_chips)
                elif dealer_hand.value > player_hand.value:
                    dealer_wins(player_hand,dealer_hand,player_chips)
                elif dealer_hand.value < player_hand.value:
                    player_wins(player_hand,dealer_hand,player_chips)
                else:
                    push(player_hand,dealer_hand)

            # Look at players total chips
            print('Players total wins are: ',player_chips.total)

            new_game = input('Do you want to play again? Enter y/n')
            if new_game[0].lower=='y':
                isPlaying = True
                continue
            else:
                print('Thanks for playing!')
                break
                
