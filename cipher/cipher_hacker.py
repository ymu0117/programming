from programming.cipher.base import Hacker
from programming.cipher.cipher_engine import CaesarCipher, TranspositionCipher, TranspositionCipherArr


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


def transposition_hacking(my_bytes, dictionary, percent, key_range):
    """Hacking transpositionCipher. 
    """
    for k in range(1, key_range):
        inst = TranspositionCipher(k, word='null')
        try:
            decrypted_txt = inst.decrypt(my_bytes)
        except:
            continue
        words = decrypted_txt.split(' ')
        words_percent = calc_percent(words, dictionary)
        if words_percent > percent:
            return k 


def transposition_arr_hacking(my_bytes, dictionary, percent, key_range):
    """Hacking transpositionCipherArr. 
    """
    for k in range(1, key_range):
        key = (k, '_') 
        inst = TranspositionCipherArr(key)
        try: 
            decrypted_txt = inst.decrypt(my_bytes)
        except:
            continue 
        words = decrypted_txt.split(' ')
        words_percent = calc_percent(words, dictionary)
        if words_percent > percent:
            return k 
    
