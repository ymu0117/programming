from abc import ABC, abstractmethod


class Cipher(ABC):
    """
    Base class for cryptocryphy
    """
    def __init__(self):
        pass

    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass


class Hacker(ABC):
    """
    Base class for hacking ciphertext 
    """
    def __init__(self):
        pass

    @abstractmethod
    def hacking(self):
        pass 

