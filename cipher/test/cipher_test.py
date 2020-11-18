import pytest
from programming.cipher import cipher_engine
from programming.cipher.word import load_dictionary, load_Webster
from programming.cipher.cipher_hacker import bruteforcehacking 


def test_CaesarCipher_bytes():
    plaintext = 'abc'
    inst = cipher_engine.CaesarCipher(key=3000)
    ciphertext = inst.encrypt(plaintext)
    decrypted_txt = inst.decrypt(ciphertext)
    assert decrypted_txt == plaintext


def test_CaesarCipher_bytes_unicode():
    plaintext = 'αβγ'
    inst = cipher_engine.CaesarCipher(key=300)
    ciphertext = inst.encrypt(plaintext)
    decrypted_txt = inst.decrypt(ciphertext)
    assert decrypted_txt == plaintext


def test_CaesarCipher_bytes_paragraph():
    plaintext = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
                "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
                "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
                "except the key, is public knowledge.")
    inst = cipher_engine.CaesarCipher(key=1000)
    ciphertxt = inst.encrypt(plaintext)
    decrypted_txt = inst.decrypt(ciphertxt)
    assert decrypted_txt == plaintext


def test_CaesarCipher_bytes_3():
    plaintxt = 'abcd'
    inst = cipher_engine.CaesarCipher(key=3)
    decrypted_txt = inst.decrypt(inst.encrypt(plaintxt))
    assert decrypted_txt == plaintxt


def test_CaesarCipher_bytes_27():
    plaintxt = 'None9👍'
    inst = cipher_engine.CaesarCipher(key=2)
    decrypted_txt = inst.decrypt(inst.encrypt(plaintxt))
    assert decrypted_txt == plaintxt


def test_CaesarCipher_bytes_1():
    plaintxt = '🐍'
    inst = cipher_engine.CaesarCipher(key=1)
    decrypted_txt = inst.decrypt(inst.encrypt(plaintxt))
    assert decrypted_txt == plaintxt


def test_CaesarCipher_bytes_7():
    plaintxt = '😁😛😋🤣'
    inst = cipher_engine.CaesarCipher(key=7)
    decrypted_txt = inst.decrypt(inst.encrypt(plaintxt))
    assert decrypted_txt == plaintxt


def test_CaesarCipher_bytes_0():
    plaintxt = 'abc'
    inst = cipher_engine.CaesarCipher(key=0)
    decrypted_txt = inst.decrypt(inst.encrypt(plaintxt))
    assert decrypted_txt == plaintxt


def test_bruteforcehacking():
    plaintext = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
                "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
                "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
                "except the key, is public knowledge.")
    inst = cipher_engine.CaesarCipher(key=20)
    ciphertxt = inst.encrypt(plaintext)
    # load Webster dictionary 
    path = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.json'
    dictionary = load_Webster(path) 
    percent = 0.5
    key_range = 1000
    key = bruteforcehacking(ciphertxt, dictionary, percent, key_range)
    assert key == 20 



