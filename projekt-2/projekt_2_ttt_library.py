#!/usr/bin/python

# last edit:    2024-09-28  19:30
"""
modul s funkcemi pro projekt_2_tictactoe.py 

autor:    Daniel Mazur
e-mail:   daniel.mazur.cz@gmail.com
discord:  daniel_67828

"""
from sys import exit  # to use sys.exit() for program termination

double_bar = "============================================"

playing_grid = """+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+"""
# This is improved over the problem statement, because it shows numbers of
# the slots, where one aims to put their X or O, and also it is full-width
# in fixed-width font and not "collapsed".
# The method of putting in X and O is by *replacing* the numbers with the
# marks. Not inserting.

def print_grid_mapping(grid):
    print(grid.find('1'), grid.find('2'), grid.find('3'))
    print(grid.find('4'), grid.find('5'), grid.find('6'))
    print(grid.find('7'), grid.find('8'), grid.find('9'))    

def refresh_grid_mapping(grid):
    grid_map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for a in range(1,10):
        grid_map[a] = grid.find(str(a))
    
    #print(*grid_map)
    return(grid_map)

def get_fresh_grid():
    return(playing_grid)

grid_map = [0, 16, 20, 24, 44, 48, 52, 72, 76, 80] # positions of numbers
            # in playing_grid
def get_grid_map():
    return(grid_map)

game_template = ["", "", "", "", "", "", "", "", "", ""]
def get_grid_template():
    return(game_template)

#-----------------------------------------------------------------------------
# function for putting a symbol at a given position in a playing board
# defined by global playing_grid (all inputs are str)
def placeSymbol(input_grid, position, symbol) -> str: 
    output = input_grid.replace(position, symbol)
    
    return(output)
# enddef

#-----------------------------------------------------------------------------
# function evaluates game grid for victory of a symbol
def did_symbol_win(input_grid, symbol):
    global grid_map
    global game_template
    map = game_template
    
    for a in range(1, 10):
        map[a] = input_grid[grid_map[a]]

    #print(*map) 

    # winning combinations are: 123, 456, 789, 147, 258, 369, 159, and 357
    if (map[1] == symbol) and (map[2] == symbol) and (map[3] == symbol):
        return(True)
    if (map[4] == symbol) and (map[5] == symbol) and (map[6] == symbol):
        return(True)
    if (map[7] == symbol) and (map[8] == symbol) and (map[9] == symbol):
        return(True)
    if (map[1] == symbol) and (map[4] == symbol) and (map[7] == symbol):
        return(True)
    if (map[2] == symbol) and (map[5] == symbol) and (map[8] == symbol):
        return(True)
    if (map[3] == symbol) and (map[6] == symbol) and (map[9] == symbol):
        return(True)
    if (map[1] == symbol) and (map[5] == symbol) and (map[9] == symbol):
        return(True)
    if (map[3] == symbol) and (map[5] == symbol) and (map[7] == symbol):
        return(True)
    #endif

    return(False)
# enddef

def get_valid_position(grid, prompt) -> str:
    valid = False
    while not valid:
        print(double_bar)
        position = input(prompt)

        if (position.isdigit()) and (int(position) in range(1, 10)):
            if (grid.find(position) != -1):   # means the position number
                # has not yet been overwritten with X or O
                valid = True
            else:
                print("This position is already taken, try another.")
            #endif
        else:
            print("This is not a valid position number, try again.")
        #endif

    #endwhile
    print(double_bar)
    return(position)
#enddef

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    #print_grid_mapping(playing_grid)
    refresh_grid_mapping(playing_grid)





