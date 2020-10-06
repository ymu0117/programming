

def _reverseCipher(plaintext):
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


class Cipher(object):
    """
    The Cipher class has functionalities such as encrypt and decrypt the ciphertext.
    """
    def __init__(self, key=None):
        self.key = key

    def encrypt(self):
        raise NotImplementedError

    def decrypt(self):
        raise NotImplementedError


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

