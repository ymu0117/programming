from programming.cipher.base import Cipher


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






