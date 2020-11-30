from cipher.base import Hacker
from cipher.cipher_engine import CaesarCipher, TranspositionCipherArr
from string import ascii_lowercase
from random import choice 
import re
import warnings 


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


def substitution_hacking(ciphertxt:str, pattern_map:dict)->str:
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

    solved_mapping, unsolved_mapping = get_solved_mapping(intersected_table) 

    decrypted_txt = convert_txt(ciphertxt, solved_mapping)

    return decrypted_txt 


class SubstitutionHacker(Hacker):

    def __init__(self):
        pass

    def hacking(self):
        pass 
    
