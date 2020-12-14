from cipher.base import Hacker
from cipher.cipher_engine import CaesarCipher, TranspositionCipherArr
from string import ascii_lowercase
from random import choice
import re
import warnings
from cipher.utils import calc_percent, find_factors, verify_case, word2pattern, create_pattern_map, \
    txt2words, get_intersected_table, get_solved_mapping, convert_txt, word2table, reduce_unsolved_mapping


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
    candidate_key_len = find_factors(len(my_bytes))
    for k in candidate_key_len:
        word = ''.join(choice(ascii_lowercase) for i in range(k))
        key = (k, word)
        inst = TranspositionCipherArr(key)
        decrypted_txt = inst.decrypt(my_bytes)
        words = decrypted_txt.split(' ')
        words_percent = calc_percent(words, dictionary)
        if words_percent > percent:
            return k


def substitution_hacking(ciphertxt, dictionary, case_type, alphabet):
    pattern_map = create_pattern_map(dictionary, case_type)
    words = txt2words(ciphertxt)

    tables = []
    for w in words:
        table = word2table(w, case_type, pattern_map, alphabet)
        tables.append(table)

    intersected_table = get_intersected_table(tables, alphabet)
    solved_mapping, unsolved_mapping = get_solved_mapping(intersected_table)
    solved_mapping, unsolved_mapping = reduce_unsolved_mapping(solved_mapping, unsolved_mapping)
    hacked_txt = convert_txt(ciphertxt, solved_mapping, case_type)
    return hacked_txt, solved_mapping, unsolved_mapping

