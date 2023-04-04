import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if value == 11:
            self.face = 'Jack'
        if value == 12:
            self.face = 'Queen'
        if value == 13:
            self.face = 'King'
        if value == 14:
            self.face = 'Ace'
        self.dealt = False 

class Player:
    def __init__(self, stack):
        self.cards = []
        self.stack = stack
        
        self.big_blind = False
        self.small_blind = False

def deck():
    deck_list = []
    suit = ['Spade', 'Club', 'Heart', 'Diamond']
    for i in suit:
        for j in range(2, 15):
            deck_list.append(Card(i, j))
    random.shuffle(deck_list)
    return deck_list

def get_cards(game_deck, players):
    deck_pos = 0
    for i in range(2):
        for player in players:
            player.cards.append(game_deck[deck_pos])
            game_deck[deck_pos].dealt = True
            deck_pos += 1

def deal(game_pos, game_deck, table):
    if game_pos == 'flop':
        flop = 0
        found_burn_card = False

        for card in game_deck:
            if found_burn_card == True:
                break
            if card.dealt == True:
                continue
            else:
                found_burn_card = True
                card.dealt = True

        for card in game_deck:
            if card.dealt == True:
                continue
            else:
                if flop == 3:
                    break
                else:
                    table.append(card)
                    flop += 1
    elif game_pos == 'turn':
        print('its the turn')
    elif game_pos == 'river':
        print('its the river')







def bet_round(players):
    for index, player in enumerate(players):
        if player.big_blind == True:
            print('Please make sure no one is watching. Player,' index,' are you ready to see your cards? (Y/N)')
            check_cards = input()
            if check_cards == 'Y':
                print('First Card:', player.cards.suit[0], player.cards.value[0], 'Second Card:', player.cards.suit[1], player.cards.value[1])
            print('You are the big blind so you must go first. Would you like to bet (1), fold (2), or see your cards again (3)? (1, 2, 3)')
            choice = int(input())
            #if choice == 1:
            #if choice == 2:
            #if choice == 3:

#def response_round():

def poker_round():
    print('Welcome to Poker. Please enter how many players:')
    num_players = int(input())
    print('Please enter how much starting money for each player:')
    starting_stack = input()
    print('The game will now start with', num_players, 'players in the hand. Best of Luck!')

    game_deck = deck()
    players = []
    for i in range(num_players):
        players.append(Player(starting_stack))
    get_cards(game_deck, players)
    players[0].big_blind == True
    players[1].small_blind == True
    #bet_round()
    #response_round()
    table = []
    deal('flop', game_deck, table)
    #bet_round()
    #response_round()
    deal('turn', game_deck, table)
    #bet_round()
    #response_round()
    deal('river', game_deck, table)
    #bet_round()
    #response_round()
    #showdown()
    #move amounts to who won, and split pot if they are equal value

if __name__ == '__main__':

    """ 
    game_deck = deck()
    players = []
    for i in range(2):
        players.append(Player(500))
    get_cards(game_deck, players)
    table = []
    deal(game_deck, table)
    """
    
    poker_round()
