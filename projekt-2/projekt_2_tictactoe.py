#!/usr/bin/python

# last edit:    2024-09-28  19:30
"""
projekt_2_tictactoe.py: Tic-tac-toe (piškvorky, 3x3 array)

autor:    Daniel Mazur
e-mail:   daniel.mazur.cz@gmail.com
discord:  daniel_67828
|-----------------------------------------------------------------------------|

"""
from sys import exit  # to use sys.exit() for program termination

import projekt_2_ttt_library as ttt

hithere = """Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================"""

letsplay = """Let's start the game
--------------------------------------------"""

double_bar = "============================================"

itsadraw = "Sorry, you tied. There is no winner."

keep_playing = True
game_finished = False

print(hithere)

while keep_playing:
    # game only provides the HUMAN vs. HUMAN mode
    game_finished = False
    game_step = 0
    mygrid = ttt.get_fresh_grid()
    print(letsplay)
    print(mygrid)

    while not game_finished:
        game_step += 1
        if (game_step % 2) == 1:    # 'O' always starts
            symbol = "O"
        else:
            symbol = "X"
        
        #print(double_bar)
        prompt = f"Player {symbol} | Please enter your move number: "
        #position = input(prompt)
        # Here I still need to verify the input(), or rather use a 
        # different, custom 'input' function:
        #   * is it an int between 1 and 9 inclusive
        #   * has this int NOT been used before
        # If any of the two checkcs fails, I need to require another,
        #   correct input.
        #print(double_bar)
        position = ttt.get_valid_position(mygrid, prompt)

        mygrid = ttt.placeSymbol(mygrid, position, symbol)
        print(mygrid)

        game_finished = ttt.did_symbol_win(mygrid, symbol)
        #print(double_bar)

        if game_finished:
            victory = f"Congratulations, the player {symbol} WON!"
            print(double_bar)
            print(victory)
            print(double_bar)
        #endif

        if game_step == 9 and not game_finished:
            game_finished = True
            print(itsadraw)
        #endif
    #endwhile
    if not ((input("Keep playing (y/other)? ")).upper() == "Y"):
        keep_playing = False
    print(double_bar)
#endwhile


























# endcode