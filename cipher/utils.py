"""
Define helper functions 
"""
import math 
import re 


def convert_2d_list(my_list, key, word):
    """Convert 1d list to 2d list, 
    each row has key elements and pad with word 
    to make rectangular shape. 
    """
    remainder = len(my_list) % key
    my_list.extend([word] * remainder)
    num_rows = len(my_list) // key
    two_d_list = [[my_list[j*key+i] for i in range(key)] for j in range(num_rows)] 
    return two_d_list


def transpose_2d_list(two_d_list):
    """Transpose 2d list. 
    """
    row = len(two_d_list)
    col = len(two_d_list[0])
    if row <= 1 or col <= 1:
        raise ValueError('List need to be two d to make transpose.')
    return [[two_d_list[x][y] for x in range(row)] for y in range(col)]


def convert_1d_list(two_d_list):
    """Convert two dimensional list to one dimension and remove padding words. 
    """
    row = len(two_d_list)
    col = len(two_d_list[0]) 
    return [two_d_list[x][y] for x in range(row) for y in range(col) if not isinstance(two_d_list[x][y], str)]


def convert_transpose_2d(my_list, key, word):
    """Convert transposition cipher to 2 d list. 
    """
    remainder = key - len(my_list) % key
    col = math.ceil(len(my_list)/key)
    two_d_list = [[None for x in range(col)] for y in range(key)]
    for k in range(key):
        if k < (key - remainder):
            two_d_list[k] = my_list[k*col:(k+1)*col]
        else:
            start = (key-remainder)*col+(k-key+remainder)*(col-1)
            two_d_list[k] = my_list[start:start+(col-1)]
            two_d_list[k].append(word)
    return two_d_list


def calc_percent(words, dictionary):
    count = 0
    for x in words:
        if x.lower() in dictionary:
            count += 1
    return count / len(words)


def simple_extract_words(txt):
    """Extracting words using re, assuming white space and symbols 
    are preserved when being entryped  
    """
    return re.findall(r'\w+', txt)





