from programming.cipher.base import Hacker
from programming.cipher.cipher_engine import CaesarCipher, TranspositionCipherArr
from string import ascii_lowercase
from random import choice 


def calc_percent(words, dictionary):
    count = 0
    for x in words:
        if x.lower() in dictionary:
            count += 1
    return count / len(words)


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


