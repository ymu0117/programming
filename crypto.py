import os
import yaml

from random import choice

from sans_program_project.cipher import Cipher


def _reverseCipher(plaintext):
    # ciphertext = list(reversed(plaintext))
    # return ''.join(ciphertext)
    ciphertext = plaintext[::-1]
    return ciphertext


def _rotate(l, n):
    """
    Parameters
    ----------
    text: list of characters
    n: int
    """
    return l[n:] + l[:n]


generic_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def _generic_rotate(my_bytes, n):
    """
    Parameters
    ----------
    my_bytes: bytes
    n: int
    """
    shifted_bytes = []
    for i in range(len(my_bytes)):
        if my_bytes[i] <= 122 and my_bytes[i] >= 97:
            shifted_bytes.append(((my_bytes[i] - 97) + n) % 26 + 97)
        elif my_bytes[i] <= 90 and my_bytes[i] >= 65:
            shifted_bytes.append(((my_bytes[i] - 65) + n) % 26 + 65)
        else:
            shifted_bytes.append(my_bytes[i])
    return bytes(shifted_bytes)


class ReverseCipher(Cipher):
    """
    Using simplest cryptography algorithm, the reverse cipher.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def encrypt(self, plaintext):
        return _reverseCipher(plaintext)

    @classmethod
    def decrypt(self, ciphertext):
        return _reverseCipher(ciphertext)


class ReverseCipherByte(Cipher):
    """
    Extend ReverseCipher so that it treats the string as a byte string
    and reverses the order of bytes instead of each alphabet letter.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def encrypt(self, plaintext):
        plaintext = plaintext.encode()
        return _reverseCipher(plaintext)

    @classmethod
    def decrypt(self, ciphertext):
        ciphertext = ciphertext.encode()
        return _reverseCipher(ciphertext)


class CaesarCipher(Cipher):
    """
    Caesar Cipher is a simple substitution cipher that shifts by k in
    the alphabet, the cipher key. For example, with k=3, and English
    alphabet, 'abyz' is mapped to 'debc'.
    """
    def __init__(self, shift, **kwargs):
        super().__init__(**kwargs)
        self.shift = shift

    def encrypt(self, plaintext):
        rotated_alphabet = _rotate(generic_alphabet, self.shift)
        return ''.join([rotated_alphabet[generic_alphabet.index(x)] for x in plaintext])

    def decrypt(self, ciphertext):
        rotated_alphabet = _rotate(generic_alphabet, -self.shift)
        return ''.join([rotated_alphabet[generic_alphabet.index(x)] for x in ciphertext])


class CaesarCipherGeneric(Cipher):

    def __init__(self, shift, n_keys=8, **kwargs):
        super().__init__(**kwargs)
        self.shift = shift
        self.n_keys = n_keys
        self.kfile = os.path.dirname(os.path.realpath(__file__))

    def gen_keys(self, keys=None):
        if keys is None:
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_!@#$%^&*abcdefghijklmnopqrstuvwxyz'
            keys = ''.join(choice(chars) for _ in range(self.n_keys))
            pwd_dict = {'password': keys}
        else:
            if isinstance(keys, str):
                pwd_dict = {'password': keys}
            else:
                raise ValueError('Input keys needs to be in the string format.')

        with open(self.kfile+'/key.yaml', 'w') as file:
            yaml.dump(pwd_dict, file)

    def compare_keys(self, input_keys):
        with open(self.kfile+'/key.yaml') as file:
            keys = yaml.load(file)
        if input_keys == keys['password']:
            return True
        else:
            return False

    def encrypt(self, plaintext, keys):
        if self.compare_keys(keys):
            print('Password is correct!')
        else:
            raise ValueError('Password is incorrect.')

        if isinstance(plaintext, str):
            my_bytes = plaintext.encode()
        elif isinstance(plaintext, bytes):
            my_bytes = plaintext
        else:
            raise ValueError('Input file for plaintext should be in the format of eighter string or bytes.')
        rotated_bytes = _generic_rotate(my_bytes, self.shift)
        return rotated_bytes.decode('utf-8')

    def decrypt(self, ciphertext, keys):
        if self.compare_keys(keys):
            print('Password is correct!')
        else:
            raise ValueError('Password is incorrect.')

        if isinstance(ciphertext, str):
            my_bytes = ciphertext.encode()
        elif isinstance(ciphertext, bytes):
            my_bytes = ciphertext
        else:
            raise ValueError('Input file for ciphertext should be in the format of eighter string or bytes.')
        rotated_bytes = _generic_rotate(my_bytes, -self.shift)
        return rotated_bytes.decode('utf-8')

