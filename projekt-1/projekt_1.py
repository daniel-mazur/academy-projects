#!/usr/bin/python

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
def inputSanitized(prompt):
    my_input = input(prompt)
    if my_input.isnumeric():
        if int(my_input) in range(ntexts):
            return my_input
        else:
            print("not a number or not in range, terminating the program.")
            exit()
        # endif
    # endif

#-----------------------------------------------------------------------------
# MAIN section
# access authorization section
iddb = {    # username:password database as a dictionary
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

mid = input("username:")
mpw = getpass("password:")

if not mid in iddb.keys():
    print("unregistered user, terminating the program..")
    exit()
#endif

if not mpw == iddb.get(mid):
    print("password does not match username, terminating the program..")
    exit()
#endif

print('-' * 40)        
print("Welcome to the app, " + mid)
ntexts = len(TEXTS)
print("We have " + str(ntexts) + " texts to be analyzed.")
print('-' * 40)

ind = 0
stripChars = str.maketrans("","",".,-")

prompt = "Enter a number btw. 1 and " + str(ntexts) + " to select: "
while ind in range(ntexts): 
    # terminates program if value is outside
    # the number of texts in TEXTS list 
    # ind = int(input(prompt)) - 1
    
    user_input = input(prompt)
    if user_input.isnumeric():
        if int(user_input) in range(ntexts):
            ind = int(user_input) - 1
        else:
            print("number or not in range, terminating the program.")
            exit()
        # endif
    else:
        print("not a number, terminating the program.")
        exit()
    # endif

    print('-' * 40)  
    # if not ind in range(ntexts):
    #     print("number not in range, terminating the program..")
    #     exit()
    # #endif
 
    #wtx = TEXTS[ind]   # valid text selected

    # there are several ways to do this:
    #    https://www.geeksforgeeks.org/iterate-over-words-of-a-string-in-python/
    # we use one, which does NOT need regex
    wlist = TEXTS[ind].translate(stripChars).split()
    print(wlist)
    print(getTextStatString(wlist))

    print(getCharcountHistogram(wlist))

# endwhile



















#---------------------------------------------------------
