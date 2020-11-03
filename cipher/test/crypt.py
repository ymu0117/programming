import pytest
from programming.cipher import cipher_engine
from programming.cipher.base import Cipher
from programming.cipher.cipher_hacker import CipherHackerBruteForce
from programming.cipher.word import load_dictionary


def test_ReverseCipher():
    plaintext = 'hello world'
    inst = cipher_engine.ReverseCipher()
    assert inst.encrypt(plaintext) == 'dlrow olleh'


def test_ReverseCipherBytes():
    plaintext = 'hello world'
    inst = cipher_engine.ReverseCipherByte()
    assert inst.encrypt(plaintext) == 'dlrow olleh'


def test_CaesarCipher():
    inst1 = cipher_engine.CaesarCipher(key=3)
    assert inst1.encrypt('abcd') == 'defg'
    assert inst1.decrypt('defg') == 'abcd'


def test_CaesarCipher_key3():
    inst2 = cipher_engine.CaesarCipher(key=3)
    ciphertext = inst2.encrypt('Hello, World!')
    assert inst2.decrypt(ciphertext) == 'Hello, World!'


def test_CaesarCipher_key0():
    inst3 = cipher_engine.CaesarCipher(key=0)
    assert inst3.encrypt('Hello, World!') == 'Hello, World!'
    assert inst3.decrypt('Hello, World!') == 'Hello, World!'


def test_CaesarCipher_key100():
    inst4 = cipher_engine.CaesarCipher(key=100)
    ciphertext = inst4.encrypt('Hello, World!')
    assert inst4.decrypt(ciphertext) == 'Hello, World!'


def test_CaesarCipher_key3000():
    inst5 = cipher_engine.CaesarCipher(key=3000)
    test = inst5.encrypt('Hello, World!')
    assert inst5.decrypt(test) == 'Hello, World!'


def test_CaesarCipher_alphabeta():
    plaintext = 'αβγδεζηθικλμνξοπρςστυφχψ'
    inst6 = cipher_engine.CaesarCipher(key=3)
    test = inst6.encrypt(plaintext)
    assert inst6.decrypt(test) == 'αβγδεζηθικλμνξοπρςστυφχψ'


def test_CaesarCipher_Emojis():
    plaintext = '\U0001f600\U0001F606\U0001F923'    # Emojis
    inst7 = cipher_engine.CaesarCipher(key=30)
    test = inst7.encrypt(plaintext)
    assert inst7.decrypt(test) == plaintext


def test_CipherHackerBruteForce_helloworld():
    plaintext = 'hello world'
    inst = cipher_engine.CaesarCipher(key=5)
    ciphertext = inst.encrypt(plaintext)
    # load dictionary 
    path = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
    dictionary = load_dictionary(path)
    
    inst = CipherHackerBruteForce(dictionary,
                                  percent=0.5,
                                  key_range=20,
                                  separator=' ')

    keys = inst.hacking(ciphertext)

    key_list = [x for x in keys.keys()]
    assert 5 in key_list 


def test_CipherHackerBruteForce_helloworld_key1000():
    plaintext = 'hello world'
    inst = cipher_engine.CaesarCipher(key=1000)
    ciphertext = inst.encrypt(plaintext)
    # load dictionary 
    path = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
    dictionary = load_dictionary(path)
    
    inst = CipherHackerBruteForce(dictionary,
                                  percent=0.5,
                                  key_range=2000,
                                  separator=' ')

    keys = inst.hacking(ciphertext)

    key_list = [x for x in keys.keys()]
    assert 1000 in key_list


def test_CipherHackerBruteForce_emoji_key50():
    plaintext = 'hello world \U0001f600 \U0001F606 \U0001F923'
    inst = cipher_engine.CaesarCipher(key=2)
    ciphertext = inst.encrypt(plaintext)
    # load dictionary 
    path = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
    dictionary = load_dictionary(path)
    inst = CipherHackerBruteForce(dictionary,
                                  percent=0.5,
                                  key_range=2000,
                                  separator=' ')

    keys = inst.hacking(ciphertext)

    key_list = [x for x in keys.keys()]
    assert 2 in key_list
    
