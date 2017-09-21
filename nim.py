"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000

def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    
    # Insert your code here
    final_move=0
    final_won=0
    for dummy_move in range(1,4):
        total_moves=100000
        total_won=0
        for move in range(0,total_moves):
            total_count=num_items-dummy_move
            final_chance=0
            while(total_count>0):
                final_chance=(final_chance+1)%2
                total_count=total_count-random.randrange(1,4)
            if(final_chance==0):
                total_won=total_won+1
        if(total_won>final_won):
            final_move=dummy_move
            final_won=total_won        
    return final_move


def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

play_game(21)
       
    
                 
    