from programming.cipher.cipher import Cipher


def _reverseCipher(plaintext):
    ciphertext = plaintext[::-1]
    return ciphertext


def _caesar_encrypt(text, key):
    """
    Parameters
    ----------
    text: string text 
        
    Returns 
    -------
    shifted_str: string text after shifted code points.
    """
    shifted_cp = []     # shifted code point 
    for t in text:
        if ord(t) > 1114111:
            raise ValueError('The input character is beyond the range of Unicode encoding.')
        shifted_cp.append((ord(t) + key) % 1114112)      # utf-8 is one of Unicode encoding schemes, which has 1114112 possible code points  
    shifted_str = ''.join([chr(x) for x in shifted_cp])
    return shifted_str


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

        shifted_str = _caesar_encrypt(plaintext, self.key)

        return shifted_str 

    def decrypt(self, ciphertext):

        shifted_str = _caesar_encrypt(ciphertext, -self.key)

        return shifted_str 

