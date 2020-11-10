from programming.cipher.base import Hacker
from programming.cipher.cipher_engine import _shift_code_points
from collections import defaultdict 


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
        code_points = _shift_code_points(my_bytes, -k)
        decrypted_txt = code_points.decode()           # decode is only compatible with ASCII and will raise error if out of range. 
        words = decrypted_txt.split(' ')
        words_percent = calc_percent(words, dictionary)
        if words_percent > percent:
            return k
    return 0 
            
