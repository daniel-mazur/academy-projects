#!/usr/bin/python
# last edit:    2024-08-24  15:30
"""
projekt_1.py: Textový analyzátor

autor:    Daniel Mazur
e-mail:   daniel.mazur.cz@gmail.com
discord:  daniel_67828

"""
from getpass import getpass # to input password without displaying it
from sys import exit  # to use sys.exit() for program termination

from task_template import TEXTS
from projekt_1_stat_funcs import *

#-----------------------------------------------------------------------------
# local functions
def inputSanitized(prompt) -> str:
    # sanitizes input, lets through only integer, if in range from 0 
    # to num_of_texts-1 (num_of_texts is global, derived from imported TEXTS)
    my_input = input(prompt)
    if my_input.isnumeric():
        if int(my_input) in range(num_of_texts):
            return my_input
        else:
            print("not a number or not in range, terminating the program.")
            exit()
        # endif
    # endif

#-----------------------------------------------------------------------------
# MAIN section
# access authorization section
id_database = {    # username:password database as a dictionary
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

user_id = input("username:")
user_password = getpass("password:")

if not user_id in id_database.keys():
    print("unregistered user, terminating the program..")
    exit()
#endif

if not user_password == id_database.get(user_id):
    print("password does not match username, terminating the program..")
    exit()
#endif

# initialization section
num_of_texts = len(TEXTS)

# user interaction section
print('-' * 40)        
print("Welcome to the app, " + user_id)
print("We have " + str(num_of_texts) + " texts to be analyzed.")
print('-' * 40)

ind = 0 # only start value to enter while-loop, later hold index of text to
        # be analyzed
stripChars = str.maketrans("","",".,-") # this is a filter to strip punctuation
                                        # from a given text

# 'prompt' is used mainly so we can stick to 80-character lines, despite
# using explicitly named (hence very long-named) variables and functions
prompt = "Enter a number btw. 1 and " + str(num_of_texts) + " to select: "
while ind in range(num_of_texts): 
    # terminates program if value is outside
    # the number of texts in TEXTS list 
    # ind = int(input(prompt)) - 1
    
    user_input = input(prompt)
    if user_input.isnumeric():
        ind = int(user_input) - 1
        if ind not in range(num_of_texts):
            print("number not in range, terminating the program.")
            exit()  # note: if exit() is inside a function instead of main
                    # code, the program still raises error, because of
        # endif     # return value type mismatch; so inputSanitized() is
    else:           # useless 
        print("not a number, terminating the program.")
        exit()
    # endif

    print('-' * 40)  
    # if not ind in range(num_of_texts):
    #     print("number not in range, terminating the program..")
    #     exit()
    # #endif
 
    #wtx = TEXTS[ind]   # valid text selected

    # there are several ways to do this:
    #    https://www.geeksforgeeks.org/iterate-over-words-of-a-string-in-python/
    # we use one, which does NOT need regex
    word_list = TEXTS[ind].translate(stripChars).split()
    # now word_list contains words stripped of punctuation, but beware: will
    # NOT work on non-integer numbers
    # print(word_list)
    print(getTextStatString(word_list))

    print(getCharcountHistogram(word_list))

# endwhile



















#---------------------------------------------------------
