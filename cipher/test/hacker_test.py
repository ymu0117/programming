import pytest
from programming.cipher import cipher_engine
from programming.cipher.cipher_hacker import bruteforcehacking
from programming.cipher.word import load_dictionary, load_Webster


def test_bruteforcehacking():
    plaintext = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
                 "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
                 "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
                 "except the key, is public knowledge.")
    key = 2 
    inst = cipher_engine.CaesarCipher(key=key)
    cipherbytes = inst.encrypt(plaintext)

    path = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.json'
    dictionary = load_Webster(path)

    found_key = bruteforcehacking(cipherbytes, dictionary, percent=0.5, key_range=1000) 
    assert found_key == key
