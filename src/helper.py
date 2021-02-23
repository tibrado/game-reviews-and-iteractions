# Helper class with helper functions 
import string
import re


def removeCharacters(string_):
    '''
    Parameters: 
        string (str): string with punctuations 
    
    Returns: 
        string (str): with no punctuactions
    '''
    char_list = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for s in string_:
        if s in char_list:
            string_ = string_.replace(s, ' ')

    return string_


def lower(string_):
    '''
    Parameters: 
        string (str): string  
    
    Returns: 
        string (str): all lower
    '''
    return string_.lower()


def console(name):
    '''
    Parameters: 
        string (str): string  
    
    Returns: 
        string (str): console name 
    '''
    consoles = ['wii', 'xbox', 'playstation', 'switch', 'pc', 'vr', 'dlc', 'vita', '3ds', '2ds']
    playstation = ['ps3', 'ps4', 'ps5']
    xbox = ['series x', 'series s']

    found = False # check for number of consoles 
    console = 'unknown'

    for c in consoles:
        if re.search(c,name):
            console = c

            # If there are more than one consoles 
            if found:
                return 'multi'

            found = True

    # check for playstation consoles 
    if console != 'playstation':
        for p in playstation:
            if re.search(p,name):
                console = 'playstation'
                
                # If there are more than one consoles 
                if found:
                    return 'multi'
                found = True

    # check for playstation consoles 
    if console != 'xbox':
        for x in xbox:
            if re.search(x,name):
                console = 'xbox'
                
                # If there are more than one consoles 
                if found:
                    return 'multi'
                found = True

    return console
