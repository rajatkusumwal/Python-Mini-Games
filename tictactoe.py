"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trail(current_board,player):
    """
    Plays a trail game with the given player as the one to act.
    """
    board=current_board.clone()
    if(player==provided.PLAYERX):
        current_player=provided.PLAYERX
        other_player=provided.PLAYERO
    else:
        current_player=provided.PLAYERO
        other_player=provided.PLAYERX
    counter=0
    while(len(board.get_empty_squares())!=0):
        random_move=random.randrange(0,len(board.get_empty_squares()))
        empty_squares=board.get_empty_squares() 
        row=empty_squares[random_move][0]
        col=empty_squares[random_move][1]
        if(counter%2==0):
            board.move(row,col,current_player)
            counter=(counter+1)
        else:
            board.move(row,col,other_player)
            counter=(counter+1)
        if (board.check_win()!=None):
            break
    return board

            
def mc_update_score(scores,board,player):
    if(board.check_win()==provided.DRAW):
        return
    else:
        winner=board.check_win()
        dimension=board.get_dim()
        for dummy_row in range(0,dimension):
            for dummy_col in range(0,dimension):
                if(board.square(dummy_row,dummy_col)==winner):
                    score[dummy_row][dummy_col]=score[dummy_row][dummy_col]+SCORE_CURRENT
                else:
                    score[dummy_row][dummy_col]=score[dummy_row][dummy_col]-SCORE_OTHER
    
def get_best_move(board,scores):
    empty_list=board.get_empty_squares()
    final_list=[]
    if(len(empty_list)>0):
        max_score=-9999999999
        for unit_tuple in empty_list:
            if(scores[unit_tuple[0]][unit_tuple[1]]>max_score):
                max_score=scores[unit_tuple[0]][unit_tuple[1]]
        for unit_tuple in empty_list:
            if(scores[unit_tuple[0]][unit_tuple[1]]==max_score):
                final_list.append(unit_tuple)
        return final_list[random.randrange(0, len(final_list))]
        
        
def mc_move(board,player,trials):
    global score
    for unit_trial in range(0,trials):
        current_board=mc_trail(board,player)
        mc_update_score(score,current_board,player)
    return get_best_move(board,score)

            
    
    
        
    
    

score=[]
for dummy_row in range(0,3):
    score.append([0,0,0])




# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.
provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERO, mc_move, NTRIALS, False)
