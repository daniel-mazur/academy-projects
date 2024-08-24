#!/usr/bin/python

"""
modul s funkcemi pro zpracování textu v projekt_1.py 

autor:    Daniel Mazur
e-mail:   daniel.mazur.cz@gmail.com
discord:  daniel_67828

"""
# module offers functions that produce various statistics of given texts
# that had already been transformed to lists of words (eg. using txt.split())

def wcountLowercase(wlist):
    # counts lowercase words in word list 'wlist'
    c = 0
    # for w in wlist: 
    #     if w.islower():
    #         c += 1
    #     # endif
    # # endfor
    for w in wlist:
        is_w_lowercase = True
        for char in w:
            # char-by-char test
            if not char.islower():
                is_w_lowercase = False
                break
            # endif
        # endfor
        if is_w_lowercase:
            c += 1
#            print(f"{w} is LOWERCASE.\n")
        # endif
    # endfor    
    
    return c
# enddef

def wcountUppercase(wlist):
    # counts uppercase words in word list 'wlist'
    c = 0
    # for w in wlist:
    #     if w.isupper(): # isupper() and islower() do not regard presence of
    #         c += 1      # digits as a reason for False outcome!!!
    #         print(f"{w} is UPPERCASE.\n")
    #     # endif
    # # endfor
    for w in wlist:
        is_w_uppercase = True
        for char in w:
            # char-by-char test
            if not char.isupper():
                is_w_uppercase = False
                break
            # endif
        # endfor
        if is_w_uppercase:
            c += 1
#            print(f"{w} is UPPERCASE.\n")
        # endif
    # endfor    
    
    return c
# enddef

wsum = 0.0  # global, to be exported only therough wsumNumeric() func below

def wcountNumeric(wlist):
    # counts numeric words (i.e. numbers) in word list 'wlist' and sums them
    # up in a global variable wsum
    global wsum
    wsum = 0.0   # nutné resetovat před každou další kompletní analýzou
    c = 0
    for w in wlist: 
        if w.isdigit():
            #print(f"{w} is numeric.\n")
            c += 1
            wsum += float(w)
        # endif
    # endfor
    return c
# enddef

def wcountNames(wlist):
    # counts names (i.e. titlecase words, or words with capital first
    # letter and NOT all-caps) in word list 'wlist'
    c = 0
    for w in wlist: 
        if w.isalpha() and w[0].isupper():
            c += 1
        # endif
    # endfor
    return c
# enddef

def wsumNumeric():
    # gives the value in wsum global, which 
    # had been filled by wcountNumeric()
    global wsum
    return wsum # works only if preceded by wcountNumeric() on the same text
# enddef

def getTextStatString(wlist):
    # calls text stat functions and assembles the output (multiline) string
    sout = str()
    sout = "There are " + str(len(wlist)) + " words in the selected text.\n"
    sout += "There are " + str(wcountNames(wlist)) + " titlecase words.\n"
    sout += "There are " + str(wcountUppercase(wlist)) + " uppercase words.\n"
    sout += "There are " + str(wcountLowercase(wlist)) + " lowercase words.\n"
    sout += "There are " + str(wcountNumeric(wlist)) + " numeric strings.\n"
    sout += "The sum of all the numbers is:" + str(int(wsumNumeric())) + "\n"   

    return sout
# enddef

def getCharcountHistogram(wlist):
    # counts characters in every word in word list 'wlist', fills histogram
    # list of int and transforms this list into multiline str sout, eg.
    # '''
    #  7| *                 |1
    #  8| ***********       |11
    #  9| ***************   |15
    # 10| *********         |9
    # 11| **********        |10
    # '''

    c = 0

    lhist = []
    for w in wlist: 
        
        if len(lhist) <= len(w):
            for ii in range(len(lhist),len(w)+1): # extending histogram,
                # so it can contain the currently-longest word count
                lhist.append(0)
            # endfor
        # endif
        lhist[len(w)] += 1
    # endfor

    # here to identify the biggest histogram value, needed for
    # output alignment
    hmax = 0
    for x in lhist:
        if x > hmax:
            hmax = x
        # endif
    # endfor
    # hmax now conatins the biggest histogram value
    if hmax <= 8:
        just = 10
    elif (hmax % 2) > 0:    # padded size just to be an odd number
        just = hmax + 3
    else:
        just = hmax + 2
    # endif

    sout = str()
    c = 0
    trig = False
    for x in lhist:
        if trig:
            sout += str(c).rjust(3,' ')+'|'
            stars = ""
            if x > 0:
                stars = ('*' * x) 
            #endif
            sout += stars.ljust(just,' ')+'|'+str(x) 
        else:
            if x > 0: # this is for the first (lowest-bin) non-zero
                # histogram value
                trig = True
                sout = str(c).rjust(3,' ')+'|'
                stars = ('*' * x)
                sout += stars.ljust(just,' ')+'|'+str(x)
            # endif
        # endif
        c += 1
        sout += '\n'
    # endfor
    
    # building 'table header' for sout
    #----------------------------------------
    #LEN| OCCURENCES |NR.
    #----------------------------------------
    hdr = "-" * 40
    hdr += '\n'
    if hmax <= 8:
        hdr += "LEN|OCCURENCES|NR."
    else:
        hdr += "LEN|"
        occ = "OCCURENCES".rjust(int((just+10)/2),' ').ljust(int(just),' ')
        # eg. symmetric padding, len("OCCURENCES")==10
        hdr += occ
        hdr += "|NR.\n"
    hdr += "-" * 40
    hdr += '\n'
    sout = hdr+sout
    sout += "-" * 40
    sout += '\n\n'

    return sout
# enddef



# endmodule