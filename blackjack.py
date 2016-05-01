# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
say=""
score = 0
game_deck=0
player_hand=0
dealer_hand=0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]    # create Hand object

    def __str__(self):
        ans=""  
        for i in range(len(self.hand)):
            ans+=str(self.hand[i])+" "
        return ans# return a string representation of a hand
        
    def add_card(self, card):
        self.hand.append(card)  # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        sum=0        # compute the value of the hand, see Blackjack video
        for i in range(len(self.hand)):
            sum+=VALUES[self.hand[i].rank]
        for i in range(len(self.hand)):
            if(self.hand[i].rank=='A' and sum+10<=21):
                sum=sum+10
        return sum
    def draw(self, canvas, pos):
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas,[pos[0]+i*72,pos[1]])# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]
        for su in range(len(SUITS)):
            for ra in range(len(RANKS)):
                self.deck.append(Card(SUITS[su],RANKS[ra]))
                
                
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop(0) # deal a card object from the deck
    
    def __str__(self):
        ans=""  # return a string representing the deck
        for i in range(len(self.deck)):
            ans+=str(self.deck[i])+" "


#define event handlers for buttons
def deal():
    global score,say,outcome,in_play,game_deck,player_hand,dealer_hand
    if(in_play==True):
        score-=1
        say="Player lost the last round."
    else:
        say=""
    outcome="Hit or Stand?"
    game_deck=Deck()
    player_hand=Hand()
    dealer_hand=Hand()
    game_deck.shuffle()
    player_hand.add_card(game_deck.deal_card())
    player_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    print "Players hand: " + str(player_hand)
    print "Dealer hand: " + str(dealer_hand)
       
    # your code goes here
    
    in_play = True

def hit():
    global in_play,score,player_hand,outcome,dealer_hand,game_deck,say
    if(player_hand.get_value()<=21):
        player_hand.add_card(game_deck.deal_card())
    elif(in_play==True):
        say="You have busted"
        score-=1
        outcome="New Deal?"
        in_play=False
        return
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global score,in_play,outcome,player_hand,dealer_hand,game_deck,say
    outcome="New Deal?"
    if(player_hand.get_value()>21 and in_play==True):
        say="You have busted"
        score-=1
        in_play=False
        return
    while(dealer_hand.get_value()<=17):
        dealer_hand.add_card(game_deck.deal_card())
    if(dealer_hand.get_value>21 and in_play==True):
        say="Dealer is busted"
        in_play=False
        score+=1
        reture
    elif(in_play==True):
        in_play=False
        if(player_hand.get_value()<=dealer_hand.get_value()):
            say="Dealer wins"
            score-=1
        else:
            say="Player wins"
            score+=1
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    player_hand.draw(canvas,[200,400])
    dealer_hand.draw(canvas,[200,200])
    canvas.draw_text('Blackjack', (200,50), 50, 'Black')
    canvas.draw_text('Player Hand', (100,450), 20, 'White')
    canvas.draw_text('Dealer Hand', (100,250), 20, 'White')
    canvas.draw_text(outcome, (300,350), 20, 'White')
    canvas.draw_text(say, (300,325), 20, 'White')
    canvas.draw_text("Score="+str(score), (300,150), 20, 'White')
    if(in_play==True):
        canvas.draw_image(card_back, [CARD_BACK_CENTER[0],CARD_BACK_CENTER[1]], CARD_SIZE, [200 + CARD_CENTER[0], 200 + CARD_CENTER[1]], CARD_SIZE) 
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()



# remember to review the gradic rubric