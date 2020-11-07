from abc import ABC, abstractmethod


class Cipher(ABC):
    """
    Base class for cryptocryphy
    """
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
    @abstractmethod
    def hacking(self):
        pass 
