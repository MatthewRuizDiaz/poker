import random
import os

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
        self.folded = False
        self.wager = 0

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
            elif card.dealt == True:
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
        turn = 0
        found_burn_card = False

        for card in game_deck:
            if found_burn_card == True:
                break
            elif card.dealt == True:
                continue
            else:
                found_burn_card = True
                card.dealt = True

        for card in game_deck:
            if card.dealt == True:
                continue
            else:
                if turn == 1:
                    break
                else:
                    table.append(card)
                    turn += 1
    elif game_pos == 'river':
        river = 0
        found_burn_card = False
        for card in game_deck:
            if found_burn_card == True:
                break
            elif card.dealt == True:
                continue
            else:
                found_burn_card = True
                card.dealt = True
        for card in game_deck:
            if card.dealt == True:
                continue
            else:
                if river == 1:
                    break
                else:
                    table.append(card)
                    river += 1
#EVERYTHING ABOVE HERE SHOULD BE FINE

def round_choice():
    response = 0
    print('Here are your options:')
    print('1: Look at cards and your own current wager')
    print('2: Bet')
    print('3: Check (not an option if your wager is below the min bet of the table)')
    print('4: Check each other players wager and the current min table bet')
    print('5: Fold')
    print('6: Call (make your wager the minimum bet of the table)')
    while True:
        choice = int(input())
        if choice == 1:
            os.system('cls')
            response = 1
            break
        elif choice == 2:
            response = 2
            break
        elif choice == 3:
            response = 3
            break
        elif choice == 4:
            response = 4
            break
        elif choice == 5:
            response = 5
            break
        elif choice == 6:
            response = 6
            break
        else:
            print('please select an option from the ones above. use the number and hit enter')
    return response

def find_min_bet(players):
    min_bet = 0
    for player in players:
        if player.wager > min_bet:
            min_bet == player.wager
    return min_bet


def betting(players): #should handle all cases
    print('This is the betting round. You will all be able to make choices and then respond to each others moves. NOTE: If you are big or little blind you will automatically wager 100 or 50 respectively')
    #might have to put a while true around this to ensure if someone bets that everyone must respond
    while True:
        for index, player in enumerate(players):
            #if the player folded. send a message saying they are out and move on the next player
            if player.big_blind == True:
                player.wager = 100
            elif player.little_blind == True:
                player.wager = 50
            min_bet = find_min_bet()
            print('Player', index, 'please make a choice. Make sure no one is watching if you look at your cards.')
            res = round_choice()
            if res == 1:
                print('First Card:', player.cards.suit[0], player.cards.value[0], 'Second Card:', player.cards.suit[1], player.cards.value[1], 'wager:', player.wager)
                res = round_choice()
            elif res == 2:
                print('how much do you want to wager: ')
                player.wager = player.wager + int(input()) #might not be valid
                if player.wager > min_bet:
                    min_bet = player.wager
                break
            elif res == 3:
                if player.wager >= min_bet: #might have to be ==
                    print('You check and it moves to next player.')
                    break
                else:
                    print('Your bet is not enough to stay in the hand. please match the min bet:', min_bet)
                    res = round_choice()
            elif res == 4:
                for index, player in enumerate(players):
                    print('Player', index, 'has wagered: ', player.wager)
                print('min bet is', min_bet)
                res = round_choice()
            elif res == 5:
                print('You fold your cards and are out of the round.')
                player.folded = True
                break
            elif res == 6:
                print('You wager the min bet of the table.')
                player.wager = min_bet
                break
        for player in players:
            if player.wager < min_bet:
                print('Some players have not called and must to stay in the hand. Please check your wagers and if you have wagered enough then continue to the next person by checking.')
                break
            else:
                print('This round of betting is over.')
                now_over = True
                break
        if now_over == True:
            break



def poker_round():
    print('Welcome to Poker. Please enter how many players:')
    num_players = int(input())
    print('Please enter how much starting money for each player: (blinds are default at 50/100 and cannot be changed yet)') # at this point players must keep track of their ending stacks when starting a new round
    starting_stack = input()
    print('The game will now start with', num_players, 'players in the hand. Best of Luck!')
    game_deck = deck()
    players = []
    for i in range(num_players):
        players.append(Player(starting_stack))
    get_cards(game_deck, players)
    players[0].big_blind == True #changing who are the blinds will have to be done outside of this function
    players[1].small_blind == True
    betting(players)
    #response_round()
    #should clear the console and print the table cards before everyones turn
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
