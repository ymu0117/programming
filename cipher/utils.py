"""
Define helper functions 
"""
import math 
import re
from functools import reduce 


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


def find_factors(num):
    """Find all factors of a number by using finding parity approach
    """
    return reduce(list.__add__, ([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0))


def verify_case(word, case_type):
    if case_type == 'insensitive':
        return word.lower()
    elif case_type == 'sensitive':
        return word
    else:
        raise ValueError('Case type is not defined.')


def word2pattern(word, case_type):
    """Convert word to pattern.
    For example, for word 'abandon', the pattern will
    be '0.1.0.2.3.4.2'
    Parameters
    ----------
    word: str
    """
    word = verify_case(word, case_type)
    pattern = []
    int_map = {}
    i = 0
    for w in word:
        if w not in int_map:
            int_map[w] = str(i)
            i += 1
        pattern.append(int_map[w])
    return '.'.join(pattern)


def create_pattern_map(dictionary, case_type):
    """Map words in the defined dictionary to patterns.
    """
    pattern_map = {}
    for k in dictionary.keys():
        pattern = word2pattern(k, case_type)
        if pattern not in pattern_map:
            pattern_map[pattern] = []
        pattern_map[pattern].append(k)
    return pattern_map


def txt2words(txt):
    """Using re.compile to extract words.
    """
    pattern = re.compile('[^A-Za-z\s]')
    return pattern.sub('', txt).split()


def english_check(character):
    eng_check = re.compile(r'[a-zA-Z]')

    if eng_check.match(character):
        return True 
    else:
        return False 


def word2table(word, case_type, pattern_map, alphabet):
    """Map cipherword to a dictionary, where each letter of the
    cipherword will have a list of values that correspond to the words
    in the dictionary that have same pattern.
    """
    word = verify_case(word, case_type)
    pattern = word2pattern(word, case_type)
    table = {letter: set() for letter in alphabet}
    for i, w in enumerate(word):
        try: 
            table[w] = set([candidate_word[i] for candidate_word in pattern_map[pattern]])
        except KeyError: 
            raise ValueError("Given dictionary doesnt have words matching this pattern.")
    return table


def get_intersected_table(tables, alphabet):
    intersected_table = {letter: set() for letter in alphabet}
    for letter in alphabet:
        for table in tables:
            if table[letter] and intersected_table[letter]:
                intersected_table[letter] = intersected_table[letter].intersection(table[letter])
            elif table[letter] and not intersected_table[letter]:
                intersected_table[letter] = intersected_table[letter].union(table[letter])
            else:
                continue
    return intersected_table


def get_solved_mapping(table):
    solved_map = {}
    unsolved_map = {}
    for k, v in table.items():
        if len(v) == 1:
            solved_map[k] = list(v)[0]
        else:
            unsolved_map[k] = list(v)
    return solved_map, unsolved_map


def remove_mapped(values, solved_chrs):
    """Remove those values appears in the mapped_chrs
    Parameters
    ----------
    values: list of characters
    solved_chrs: list of characters
    """
    for v in values:
        if v in solved_chrs:
            values.remove(v)
    return values 


def reduce_unsolved_mapping(solved_mapping, unsolved_mapping):
    """Remove unsolved_mapping that has been appeared in the solved_mapping. 
    """
    mapped_chrs = solved_mapping.values()
    updated_unsolved_mapping = {}
    for k, v in unsolved_mapping.items():
        if v:      # if there are elements in k, remove those in the solved ones 
            v = remove_mapped(v, mapped_chrs)
            if len(v) == 1:     # if after removal there is unique, then we found new solved mapping
                solved_mapping[k] = v[0]
            else:
                updated_unsolved_mapping[k] = v     # if not, it's still unsolved mapping 
        else:
            updated_unsolved_mapping[k] = v 
    return solved_mapping, updated_unsolved_mapping 


def convert_txt(txt, solved_map, case_type):
    converted_txt = []
    for t in txt:
        try:
            if case_type == 'insensitive' and t.isupper():
                letter = solved_map[t.lower()]
                converted_txt.append(letter.upper())
            else:
                letter = solved_map[t]
                converted_txt.append(letter)
        except KeyError:
            if not english_check(t):
                converted_txt.append(t)
            else:
                converted_txt.append('_')
                continue
    return ''.join(converted_txt)

