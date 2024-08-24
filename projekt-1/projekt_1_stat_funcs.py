#!/usr/bin/python
# last edit:    2024-08-24  15:30
"""
modul s funkcemi pro zpracování textu v projekt_1.py 

autor:    Daniel Mazur
e-mail:   daniel.mazur.cz@gmail.com
discord:  daniel_67828

"""
# module offers functions that produce various statistics of given texts
# that had already been transformed to lists of words (eg. using txt.split())

#-----------------------------------------------------------------------------
def wcountLowercase(word_list):
    # counts lowercase words in word list 'word_list'
    counter = 0
    # for w in word_list: 
    #     if w.islower():
    #         c  += 1
    #     # endif
    # # endfor
    for word in word_list:
        is_w_lowercase = True   # a flag, may be cleared, if NOT lowercase
        for char in word:
            # char-by-char test
            if not char.islower():
                is_w_lowercase = False
                break
            # endif
        # endfor
        # now info about lower-case status is contained in is_w_lowercase
        if is_w_lowercase:
            counter += 1
#            print(f"{w} is LOWERCASE.\n")
        # endif
    # endfor    
    
    return counter
# enddef

#-----------------------------------------------------------------------------
def wcountUppercase(word_list):
    # counts uppercase words in word list 'word_list'
    counter = 0
    # for w in word_list:
    #     if w.isupper(): # isupper() and islower() do not regard presence of
    #         c += 1      # digits as a reason for False outcome!!!
    #         print(f"{w} is UPPERCASE.\n")
    #     # endif
    # # endfor
    for word in word_list:
        is_w_uppercase = True
        for char in word:
            # char-by-char test
            if not char.isupper():
                is_w_uppercase = False
                break
            # endif
        # endfor
        if is_w_uppercase:
            counter += 1
#            print(f"{w} is UPPERCASE.\n")
        # endif
    # endfor    
    
    return counter
# enddef

sum_of_numeric_words = 0.0  # global, a wcountNumeric() byproduct, exported 
                            # only through wsumNumeric() function below

#-----------------------------------------------------------------------------
def wcountNumeric(word_list):
    # returns the number of numeric words (i.e. numbers) in word list
    # 'word_list' and sums them up into a global sum_of_numeric_words
    global sum_of_numeric_words

    sum_of_numeric_words = 0.0   # resetting before each run
    counter = 0
    for word in word_list: 
        if word.isdigit():
            #print(f"{w} is numeric.\n")
            counter += 1
            sum_of_numeric_words += float(word)
        # endif
    # endfor
    return counter
# enddef

#-----------------------------------------------------------------------------
def wcountNames(word_list):
    # counts names (i.e. titlecase words, or words with capital first
    # letter and NOT all-caps) in word list 'word_list'
    counter = 0
    for word in word_list: 
        if word.isalpha() and word[0].isupper():
            counter += 1
        # endif
    # endfor
    return counter
# enddef

#-----------------------------------------------------------------------------
def wsumNumeric():
    # only gives the value in sum_of_numeric_words global, which 
    # had been filled by wcountNumeric(), just an interface function
    global sum_of_numeric_words
    return sum_of_numeric_words # works only if preceded by wcountNumeric() on the same text
# enddef

#-----------------------------------------------------------------------------
def getTextStatString(word_list):
    # calls text stat functions and assembles the output (multiline) string
    sout = str()    # this hold string output of this function
    sout = "There are " + str(len(word_list)) + " words in the selected text.\n"
    sout += "There are " + str(wcountNames(word_list)) + " titlecase words.\n"
    sout += "There are " + str(wcountUppercase(word_list)) + " uppercase words.\n"
    sout += "There are " + str(wcountLowercase(word_list)) + " lowercase words.\n"
    sout += "There are " + str(wcountNumeric(word_list)) + " numeric strings.\n"
    sout += "The sum of all the numbers is:" + str(int(wsumNumeric())) + "\n"   

    return sout
# enddef

#-----------------------------------------------------------------------------
def getCharcountHistogram(word_list):
    # counts characters in every word in word list 'word_list', fills histogram
    # list of int and transforms this list into multiline str sout, eg.
    # '''
    #  7| *                 |1
    #  8| ***********       |11
    #  9| ***************   |15
    # 10| *********         |9
    # 11| **********        |10
    # '''

    counter = 0

    lhist = []  # histogram, ie. target list of counts of word lengths 
    for word in word_list: 
        
        if len(lhist) <= len(word):
            for ii in range(len(lhist),len(word)+1): # extending histogram,
                # so it can contain the currently-longest word count
                lhist.append(0)
            # endfor
        # endif
        lhist[len(word)] += 1
    # endfor
    # now word-length analysis is done, lhist contains the result 

    # here to identify the biggest histogram value hmax, needed for
    # output alignment
    hmax = 0
    for x in lhist:
        if x > hmax:
            hmax = x
        # endif
    # endfor
    # hmax now contains the biggest histogram value

    # 'just' is a parameter for formatting (padding) on-screen output
    if hmax <= 8:
        just = 10
    elif (hmax % 2) > 0:    # padded size just to be an odd number
        just = hmax + 3
    else:
        just = hmax + 2
    # endif
    #  

    sout = str()    # this hold string output of this function
    counter = 0
    trig = False    # just a flag, so that histogram is printed starting
                    # the first non-zero bin
    for x in lhist:
        if trig:
            sout += str(counter).rjust(3,' ')+'|'
            stars = ""  # contains star bar for a given bin
            if x > 0:
                stars = ('*' * x) 
            #endif
            sout += stars.ljust(just,' ')+'|'+str(x) 
        else:
            if x > 0: # this is for the first (lowest-bin) non-zero
                # histogram value
                trig = True
                sout = str(counter).rjust(3,' ')+'|'
                stars = ('*' * x)
                sout += stars.ljust(just,' ')+'|'+str(x)
            # endif
        # endif
        counter += 1
        sout += '\n'
    # endfor
    
    # building 'table header' for sout
    #----------------------------------------
    #LEN| OCCURENCES |NR.
    #----------------------------------------
    header = "-" * 40
    header += '\n'
    if hmax <= 8:
        header += "LEN|OCCURENCES|NR."
    else:
        header += "LEN|"
        occ = "OCCURENCES".rjust(int((just+10)/2),' ').ljust(int(just),' ')
        # 'occ' gives symmetrically padded, len("OCCURENCES")==10
        header += occ
        header += "|NR.\n"
    header += "-" * 40
    header += '\n'
    sout = header + sout
    sout += "-" * 40
    sout += '\n\n'

    return sout
# enddef



# endcode