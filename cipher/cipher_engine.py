from cipher.base import Cipher
from cipher.utils import convert_2d_list, transpose_2d_list, convert_1d_list, convert_transpose_2d
import math
import numpy as np
from cipher.exceptions import InvalidKey
import random
from string import ascii_lowercase


def _reverseCipher(plaintext):
    ciphertext = plaintext[::-1]
    return ciphertext


def _shift_code_points(my_bytes, n):
    """Updating bytes literals by shifting their code points by n.
    Parameters
    ----------
    my_bytes: bytes literal that are
    n: the number we need to add to the original code points; int

    Returns
    -------
    code_points: shifted code points; list of integer
    """
    code_points = []     # list of number can be converted into bytes
    for b in my_bytes:   # each byte literal can return a integer after indexing correspond to the ASCII code
        code_points.append((b + n) % 256)    # decode method can only be applied to ACSII code points
    return bytes(code_points)              # bytes operation can be applied to a list of integer but not support encoding


class ReverseCipher(Cipher):
    """
    Using simplest cryptography algorithm, the reverse cipher.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def encrypt(self, plaintext):
        return _reverseCipher(plaintext)

    def decrypt(self, ciphertext):
        return _reverseCipher(ciphertext)


class ReverseCipherByte(Cipher):
    """
    Extend ReverseCipher so that it treats the string as a byte string
    and reverses the order of bytes instead of each alphabet letter.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def encrypt(self, plaintext):
        plaintext = plaintext.encode()
        return _reverseCipher(plaintext).decode('utf-8')

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.encode()
        return _reverseCipher(ciphertext).decode('utf-8')


class CaesarCipher(Cipher):
    """
    Caesar Cipher is a simple substitution cipher that shifts by k in
    the alphabet, the cipher key. For example, with k=3, and English
    alphabet, 'abyz' is mapped to 'debc'.
    """
    def __init__(self, key, **kwargs):
        super().__init__(**kwargs)
        if key < 0:
            raise ValueError('Key has to be positive.')
        self.key = key

    def encrypt(self, plaintext):
        if isinstance(plaintext, str):
            my_bytes = bytes(plaintext, encoding='utf-8', errors='strict')
        elif isinstance(plaintext, bytes):
            my_bytes = plaintext
        return _shift_code_points(my_bytes, self.key)

    def decrypt(self, my_bytes):
        if not isinstance(my_bytes, bytes):
            raise ValueError('Input of decrypt must be bytes.')
        new_bytes = _shift_code_points(my_bytes, -self.key)
        return new_bytes.decode()


class TranspositionCipherArr(Cipher):
    """Columnar transposition using numpy arr.
    """
    def __init__(self, key: tuple, **kwargs):
        super().__init__(**kwargs)
        self.key, self.word = key

    def make_conformable_txt(self, txt: str) -> str:
        """Add chr to the plaintxt to make it conformable."""
        num_chr = len(txt)
        added_num_chr = self.key - num_chr % self.key
        if len(self.word) < added_num_chr:
            raise ValueError('Word length should be larger than key - 1.')
        txt += self.word[:added_num_chr]
        return txt

    @staticmethod
    def columnar_transposition(my_bytes: bytes, num_rows: int, num_cols: int) -> np.ndarray:
        arr = np.frombuffer(my_bytes, dtype=np.uint8)    # convert bytes to int
        reshaped_arr = arr.reshape([num_rows, num_cols])
        return np.ravel(reshaped_arr.T)     # convert int to bytes, using tobytes gives a different format

    def find_pad(self, padded_txt):
        for i in range(len(self.word)):
            if i == 0:
                idx = padded_txt.find(self.word)
            else:
                idx = padded_txt.find(self.word[:-i])
            if idx != -1:
                return idx

    def encrypt(self, plaintxt: str) -> bytes:
        plaintxt = self.make_conformable_txt(plaintxt)
        my_bytes = bytes(plaintxt, encoding='utf-8', errors='strict')
        num_rows = len(my_bytes)//self.key
        one_d_arr = self.columnar_transposition(my_bytes, num_rows, self.key)
        return one_d_arr.tobytes()

    def decrypt(self, my_bytes: bytes) -> str:
        num_rows = len(my_bytes)//self.key
        one_d_arr = self.columnar_transposition(my_bytes, self.key, num_rows)
        decrypted_bytes = one_d_arr.tobytes()
        padded_txt = decrypted_bytes.decode(encoding='utf-8')
        last_row_txt = padded_txt[-self.key:]
        idx = self.find_pad(last_row_txt)
        txt = padded_txt[:-self.key] + last_row_txt[:idx]
        return txt


class SubstitutionCipher(Cipher):
    """Substitution Cipher

    Parameters
    ----------
    key: dictionary, can only be generated from ascii_lowercase
    """
    def __init__(self, key: dict, **kwargs):
        self.key = key
        self.verify_key()
        self.reverse_key = {v: k for k, v in self.key.items()}

    def verify_key(self):
        if not ''.join(sorted(self.key.keys())) == ''.join(sorted(self.key.values())):
            raise InvalidKey

    @classmethod
    def from_alphabet(cls, alphabet):
        """Alternative constructor from alphabet.
        """
        substitution = ''.join(random.sample(alphabet, len(alphabet)))
        key = dict(zip(alphabet, substitution))
        SubstitutionCipher.verify_key(key)
        return cls(key)

    def _convert_txt(self, txt: str, key_map) -> str:
        converted_txt = []
        for t in txt:
            try:
                if t.isupper():
                    converted_txt.append(key_map[t.lower()].upper())
                else:
                    converted_txt.append(key_map[t])
            except KeyError:
                converted_txt.append(t)    # for chr not in key_map keep it as is
        return ''.join(converted_txt)

    def encrypt(self, plaintxt: str) -> str:
        return self._convert_txt(plaintxt, self.key)

    def decrypt(self, ciphertxt: str) -> str:
        return self._convert_txt(ciphertxt, self.reverse_key)


class VigenereCipher(Cipher):
    def __init__(self, key: str, **kwargs):
        self.key = key
        self.check_key()
        self.key_len = len(self.key)
        self.key_int_map = dict(zip(ascii_lowercase, range(26)))
        self.key2int()

    def check_key(self):
        """Assuming all the keys are lowercase for simplicity
        """
        if not self.key.islower():
            raise InvalidKey

    def key2int(self):
        self.ints = [self.key_int_map[x] for x in self.key]    # iceabcream = [8, 2, 0, 1, ...]
        self.negative_ints = [-self.key_int_map[x] for x in self.key]

    def shift_bytes(self, my_bytes, integers):
        all_code_points = []
        for i, code_point in enumerate(my_bytes):
            n = i % self.key_len
            new_code_point = (code_point + integers[n]) % 256
            all_code_points.append(new_code_point)
        return bytes(all_code_points)

    def encrypt(self, plaintxt):
        if isinstance(plaintxt, str):
            my_bytes = bytes(plaintxt, encoding='utf-8', errors='strict')
        elif isinstance(plaintxt, bytes):
            my_bytes = plaintxt
        return self.shift_bytes(my_bytes, self.ints)

    def decrypt(self, my_bytes):
        if not isinstance(my_bytes, bytes):
            raise ValueError('Input of decrypt must be bytes.')
        return self.shift_bytes(my_bytes, self.negative_ints).decode()


