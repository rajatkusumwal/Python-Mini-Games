"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
import user43_5kkhgdVGS2_1 as game_testsuite

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    line_len=len(line)
    new_line=[]
    final_line=[]
    
    for dummy_index in line:
        if(dummy_index > 0):
            new_line.append(dummy_index)
            
    
    for dummy_index in range(0,len(new_line)-1):
        if(new_line[dummy_index]==new_line[dummy_index+1]):
            new_line[dummy_index]=new_line[dummy_index]+new_line[dummy_index+1]
            new_line[dummy_index+1]=0
            
    for dummy_index in new_line:
        if(dummy_index > 0):
            final_line.append(dummy_index)
    
    for dummy_index in range(len(final_line),line_len):
        final_line.append(0)
            
    return final_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.board=[]
        self.board_height=grid_height
        self.board_width=grid_width
        self.reset()
        self.new_tile()
        self.new_tile()
        self.board_dict={
            UP:[],
            DOWN:[],
            LEFT:[],
            RIGHT:[]
        }
        for dummy_col in range(0,grid_width):
            self.board_dict[1].append((0,dummy_col))
            self.board_dict[2].append((grid_height-1,dummy_col))
        
        for dummy_row in range(0,grid_height):
            self.board_dict[3].append((dummy_row,0))
            self.board_dict[4].append((dummy_row,grid_width-1))
            

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        for dummy_row in range(0,self.board_height):
            dummy_list=[]
            for dummy_col in range(0,self.board_width):
                dummy_list.append(0)
            self.board.append(dummy_list)

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self.board)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.board_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.board_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        if(direction==1):
            tile_flag=False
            for dummy_col in range(0,self.board_width):
                temp_list=[]
                for dummy_row in range(0,self.board_height):
                    temp_list.append(self.board[dummy_row][dummy_col])
                final_list=merge(temp_list)
                for dummy_row in range(0,self.board_height):
                    if(self.board[dummy_row][dummy_col]!=final_list[dummy_row]):
                        tile_flag=True
                    self.board[dummy_row][dummy_col]=final_list[dummy_row]
            if(tile_flag):
                self.new_tile()
        elif(direction==2):
            tile_flag=False
            for dummy_col in range(0,self.board_width):
                temp_list=[]
                for dummy_row in range(self.board_height-1,-1,-1):
                    temp_list.append(self.board[dummy_row][dummy_col])
                final_list=merge(temp_list)
                for dummy_row in range(self.board_height-1,-1,-1):
                    if(self.board[dummy_row][dummy_col]!=final_list[self.board_height-1-dummy_row]):
                        tile_flag=True
                    self.board[dummy_row][dummy_col]=final_list[self.board_height-1-dummy_row]
            if(tile_flag):
                self.new_tile()
        elif(direction==3):
            tile_flag=False
            for dummy_row in range(0,self.board_height):
                temp_list=[]
                for dummy_col in range(0,self.board_width):
                    temp_list.append(self.board[dummy_row][dummy_col])
                final_list=merge(temp_list)
                for dummy_col in range(0,self.board_width):
                    if(self.board[dummy_row][dummy_col]!=final_list[dummy_col]):
                        tile_flag=True
                    self.board[dummy_row][dummy_col]=final_list[dummy_col]
            if(tile_flag):
                self.new_tile()
        elif(direction==4):
            tile_flag=False
            for dummy_row in range(0,self.board_height):
                temp_list=[]
                for dummy_col in range(self.board_width-1,-1,-1):
                    temp_list.append(self.board[dummy_row][dummy_col])
                final_list=merge(temp_list)
                for dummy_col in range(self.board_width-1,-1,-1):
                    if(self.board[dummy_row][dummy_col]!=final_list[self.board_width-1-dummy_col]):
                        tile_flag=True
                    self.board[dummy_row][dummy_col]=final_list[self.board_width-1-dummy_col]
            if(tile_flag):
                self.new_tile()
                      

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        temp_list=[]
        for dummy_row in range(0,self.board_height):
            for dummy_col in range(0,self.board_width):
                if(self.board[dummy_row][dummy_col]==0):
                    temp_list.append([dummy_row,dummy_col])
        
        if(len(temp_list)!=0):
            dummy_rand=random.randrange(0,len(temp_list))
            dummy_tile=random.randrange(0,100)
            if(dummy_tile<90):
                self.board[temp_list[dummy_rand][0]][temp_list[dummy_rand][1]]=2
            else:
                self.board[temp_list[dummy_rand][0]][temp_list[dummy_rand][1]]=4        
        return

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.board[row][col]=val
        return

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.board[row][col]

#game_testsuite.run_suite(TwentyFortyEight)

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
