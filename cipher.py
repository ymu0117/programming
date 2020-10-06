from abc import ABC, abstractmethod


class Cipher(ABC):
    """
    Base class for cryptocryphy
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass
