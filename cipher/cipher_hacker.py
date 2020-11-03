from programming.cipher.base import Hacker
from programming.cipher.cipher_engine import _shift_code_points


class CipherHackerBruteForce(Hacker):
    """
    Class for hacking cipher 

    Parameters 
    ----------
    dictionary: dict, dictionary used to detect plain english after hacking  
    percent: float, percentage of plain english amoung all text
    key_range: int, the range of key used for hacking 
    separator: str, the separator used for splitting words 
    """

    def __init__(self, dictionary, percent, key_range, separator, **kwargs):
        super().__init__(**kwargs)
        self.dictionary = dictionary
        self.percent = percent
        self.key_range = key_range
        self.separator = separator 

    def calc_percent(self, words):
        count = 0 
        for x in words:
            if x in self.dictionary:
                count += 1
            else:
                continue
        return count / len(words) 

    def hacking(self, ciphertext):
        potential_keys = {}
        for k in range(1, self.key_range):
            code_points = _shift_code_points(ciphertext, -k)
            decrypted_txt = ''.join([chr(x) for x in code_points])
            words = decrypted_txt.split(self.separator)
            words_percent = self.calc_percent(words)
            if words_percent > self.percent: 
                potential_keys[k] = "{:.0%}".format(words_percent)
            else:
                continue
        return potential_keys 


    




    
