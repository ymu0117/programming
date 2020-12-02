from cipher.base import Hacker
from cipher.cipher_engine import CaesarCipher, TranspositionCipherArr
from string import ascii_lowercase
from random import choice
import re
import warnings
from cipher.utils import calc_percent


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
    for k in range(1, len(my_bytes)):   # only valid input key
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


class SubstitutionHacker(Hacker):
    """
    Parameters
    ----------
    case_type: case insensitive or sensitive for hacking, options = {'insensitive', 'sensitive'}
    alphabet: the alphabet we used to hacking the ciphertxt.
    """

    def __init__(self, case_type, alphabet):
        self.case_type = case_type
        self.alphabet = alphabet     # alphabet can be decided from ciphertxt

    def verify_case(self, word):
        if self.case_type == 'insensitive':
            return word.lower()
        elif case_type == 'sensitive':
            return word
        else:
            raise ValueError('Case type is not defined.')

    def word2pattern(self, word):
        """Convert word to pattern.
        For example, for word 'abandon', the pattern will
        be '0.1.0.2.3.4.2'
        Parameters
        ----------
        word: str
        """
        word = self.verify_case(word)
        pattern = []
        int_map = {}
        i = 0
        for w in word:
            if w not in int_map:
                int_map[w] = str(i)
                i += 1
            pattern.append(int_map[w])
        return '.'.join(pattern)

    def create_pattern_map(self, dictionary):
        """Map words in the defined dictionary to patterns.
        """
        pattern_map = {}
        for k in dictionary.keys():
            pattern = self.word2pattern(k)
            if pattern not in pattern_map:
                pattern_map[pattern] = []
            pattern_map[pattern].append(k)
        return pattern_map

    @staticmethod
    def txt2words(txt):
        """Using re.compile to extract words.
        """
        pattern = re.compile('[^A-Za-z\s]')
        return pattern.sub('', txt).split()

    def word2table(self, word, pattern_map):
        """Map cipherword to a dictionary, where each letter of the
        cipherword will have a list of values that correspond to the words
        in the dictionary that have same pattern.
        """
        word = self.verify_case(word)
        pattern = self.word2pattern(word)
        table = {letter: [] for letter in self.alphabet}
        for i, w in enumerate(word):
            try:
               for candidate in pattern_map[pattern]:
                   if candidate[i] not in table[w]:
                       table[w].append(candidate[i])
            except KeyError:
                raise ValueError('Given dictionary doesnt have words matching this pattern.')
        return table

    def get_intersected_table(self, tables):
        intersected_table = {letter: [] for letter in self.alphabet}
        for letter in intersected_table.keys():
            for table in tables:
                if table[letter] and intersected_table[letter]:
                    intersected_table[letter] = list(set(intersected_table[letter]).intersection(set(table[letter])))
                elif table[letter] and not intersected_table[letter]:
                    intersected_table[letter].extend(table[letter])
                else:
                    continue
        return intersected_table

    @staticmethod
    def get_solved_mapping(table):
        solved_map = {}
        unsolved_map = {}
        for k, v in table.items():
            if len(v) == 1:
                solved_map[k] = v
            else:
                unsolved_map[k] = v
        return solved_map, unsolved_map

    def convert_txt(self, txt, solved_map):
        converted_txt = []
        for t in txt:
            try:
                if self.case_type == 'insensitive' and t.isupper():
                    letter = list(solved_map[t.lower()])[0]
                    converted_txt.append(letter.upper())
                else:
                    letter = list(solved_map[t])[0]
                    converted_txt.append(letter)
            except KeyError:
                if t == ' ':
                    converted_txt.append(t)
                else:
                    converted_txt.append('_')
                continue
        return ''.join(converted_txt)

    def hacking(self, ciphertxt, dictionary):
        pattern_map = self.create_pattern_map(dictionary)
        words = self.txt2words(ciphertxt)

        tables = []
        for w in words:
            table = self.word2table(w, pattern_map)
            tables.append(table)

        intersected_table = self.get_intersected_table(tables)
        self.solved_mapping, self.unsolved_mapping = self.get_solved_mapping(intersected_table)
        self.hacked_txt = self.convert_txt(ciphertxt, self.solved_mapping)
        return self
