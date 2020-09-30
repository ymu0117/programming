import pytest 
from program.crypto import ReverseCipher, ReverseCipherByte 


def test_ReverseCipher(): 
    plaintext = 'hello world'
    assert ReverseCipher.encrypt(plaintext) == 'dlrow olleh'

    assert ReverseCipherByte.encrypt(plaintext) == b'dlrow olleh'

