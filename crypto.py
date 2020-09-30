

def _reverseCipher(plaintext):
    ciphertext = plaintext[::-1] 
    return ciphertext


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

