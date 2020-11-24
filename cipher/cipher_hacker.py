from programming.cipher.base import Hacker
from programming.cipher.cipher_engine import CaesarCipher, TranspositionCipherArr
from string import ascii_lowercase
from random import choice 
import re
import warnings 


def calc_percent(words, dictionary):
    count = 0
    for x in words:
        if x.lower() in dictionary:
            count += 1
    return count / len(words)


def extract_pattern_map(word):
    """For a given word, return its pattern
    """
    pattern_map = {}
    i = 0
    for w in word:
        if w in pattern_map:
            continue
        else:
            pattern_map[w] = i
            i = i + 1
    return pattern_map


def word2pattern(word, ptype='case_insensitive'):
    if ptype == 'case_insensitive':
        word = word.lower() 
    pattern_map = extract_pattern_map(word)
    return '.'.join([str(pattern_map[w]) for w in word])


def create_pattern_map(dictionary:dict)->dict:
    pattern_map = {}
    for k in dictionary.keys():
        pattern = word2pattern(k)
        if pattern in pattern_map:
            pattern_map[pattern].append(k)
        else:
            pattern_map[pattern] = [k]
    return pattern_map


def simple_extract_words(txt):
    """Extracting words using re, assuming white space and symbols 
    are preserved when being entryped  
    """
    return re.findall(r'\w+', txt)


def extract_letter_mapping(word, mappings, ptype='case_insensitive'):
    if ptype == 'case_insensitive':
        word = word.lower() 

    letters = {}
    for i, w in enumerate(word):
        letters[w] = set([m[i] for m in mappings]) 
    return letters


def cipher_word2table(cipher_word, pattern_map):
    pattern = word2pattern(cipher_word)
    mappings = pattern_map[pattern]
    table = extract_letter_mapping(cipher_word, mappings)
    return table


def update_intersected_table(intersected_table, letter_map_table): 
    for k in letter_map_table.keys():
        if k in intersected_table:
            intersected_table[k] = intersected_table[k].intersection(letter_map_table[k])
        else:
            intersected_table[k] = letter_map_table[k]
    return intersected_table


def convert_txt(txt, key_map, ptype='case_insensitive'):
    converted_txt = []
    for t in txt:
        try: 
            if ptype == 'case_insensitive' and t.isupper():
                letter_list = list(key_map[t.lower()])
            else:
                letter_list = list(key_map[t])
        except KeyError:
            converted_txt.append(t)
            continue

        if len(letter_list) == 1:
            letter = letter_list[0]
        elif len(letter_list) > 1:
            letter = letter_list[0]
            warnings.warn('Warning Message: the decryption for letter {} is not unique.'.format(t)) 
        else:
            raise ValueError('No map is found for letter {}'.format(t))

        if ptype == 'case_insensitive' and t.isupper():
            converted_txt.append(letter.upper())
        else:
            converted_txt.append(letter) 
            
    return ''.join(converted_txt)


def bruteforcehacking(my_bytes, dictionary, percent, key_range):
    """
    Hacking cipher bytes using brute force method
    """
    for k in range(1, key_range):
        inst = CaesarCipher(key=k)
        try:
            decrypted_txt = inst.decrypt(my_bytes)
        except:
            continue 
        words = decrypted_txt.split(' ')
        words_percent = calc_percent(words, dictionary)
        if words_percent > percent:
            return k


def transposition_arr_hacking(my_bytes, dictionary, percent):
    """Hacking transpositionCipherArr. 
    """
    for k in range(1, len(my_bytes)):
        word = ''.join(choice(ascii_lowercase) for i in range(k))
        key = (k, word) 
        inst = TranspositionCipherArr(key)
        try:
            decrypted_txt = inst.decrypt(my_bytes)
        except ValueError:
            print("ValueError: cannot reshape array.")
            continue 
        words = decrypted_txt.split(' ')
        words_percent = calc_percent(words, dictionary)
        if words_percent > percent:
            return k 


def substitution_hacking(ciphertxt:str, pattern_map:dict, percent:float)->str:
    """Hacking Substitution Cipher."""
    words = simple_extract_words(ciphertxt)
    letter_map_tables = []
    for w in words:
        table = cipher_word2table(w, pattern_map)
        letter_map_tables.append(table)

    intersected_table = {}
    # for each common key find the intersection
    for l in range(len(letter_map_tables)):
        intersected_table = update_intersected_table(intersected_table, letter_map_tables[l])

    decrypted_txt = convert_txt(ciphertxt, intersected_table)

    return decrypted_txt 
