from sans_program_project.cipher.cipher import Cipher


def _reverseCipher(plaintext):
    # ciphertext = list(reversed(plaintext))
    # return ''.join(ciphertext)
    ciphertext = plaintext[::-1]
    return ciphertext


def _caesar_encrypt(my_bytes, n_shift):
    """
    Parameters
    ----------
    my_bytes: bytes
    n_shift: int
    """
    shifted_bytes = []
    for i in range(len(my_bytes)):
        shifted_bytes.append((my_bytes[i] + n_shift) % 128)      # utf-8 can only decode first 128 
    return bytes(shifted_bytes)


def _text2bytes(text):
    if isinstance(text, str):
        my_bytes = text.encode()
    elif isinstance(text, bytes):
        my_bytes = text
    else:
        raise ValueError('Input file for text should be in the format of eighter string or bytes.')
    return my_bytes 


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
        self.key = key

    def encrypt(self, plaintext):
        my_bytes = _text2bytes(plaintext)
        
        shifted_bytes = _caesar_encrypt(my_bytes, self.key)

        return shifted_bytes.decode('utf-8')

    def decrypt(self, ciphertext):
        my_bytes = _text2bytes(ciphertext)

        shifted_bytes = _caesar_encrypt(my_bytes, -self.key)

        return shifted_bytes.decode('utf-8')

