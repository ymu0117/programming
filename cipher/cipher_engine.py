from programming.cipher.cipher import Cipher


def _reverseCipher(plaintext):
    ciphertext = plaintext[::-1]
    return ciphertext


def _caesar_encrypt(text, key):
    """
    Parameters
    ----------
    text: text needed to be encrypted; string
    key: key used to encrypt; int 
    
    Returns 
    -------
    shifted_str: text after shifted code points; string 
    """
    code_points = []     # shifted code point 
    for t in text:
        if ord(t) > 1114111:
            raise ValueError('The input character is beyond the range of Unicode encoding.')
        code_points.append((ord(t) + key) % 1114112)      # utf-8 is one of Unicode encoding schemes, which has 1114112 possible code points  

    encrypted_text = ''.join([chr(x) for x in code_points])
    return encrypted_text


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
        if not isinstance(plaintext, str):
            raise ValueError('Plaintext must be in string format.')

        return _caesar_encrypt(plaintext, self.key)

    def decrypt(self, ciphertext):
        if not isinstance(ciphertext, str):
            raise ValueError('Ciphertext must be in string format.')

        return _caesar_encrypt(ciphertext, -self.key)


