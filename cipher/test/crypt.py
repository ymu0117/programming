import pytest
from sans_program_project.cipher import cipher_engine
from sans_program_project.cipher.cipher import Cipher
from sans_program_project.cipher.cipher_hacker import cipher_hacker 


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
    
    inst2 = cipher_engine.CaesarCipher(key=3)
    assert inst2.encrypt('Hello, World!') == 'Khoor/#Zruog$'
    assert inst2.decrypt('Khoor/#Zruog$') == 'Hello, World!'
    
    inst3 = cipher_engine.CaesarCipher(key=0)
    assert inst3.encrypt('Hello, World!') == 'Hello, World!'
    assert inst3.decrypt('Hello, World!') == 'Hello, World!'
 
    inst4 = cipher_engine.CaesarCipher(key=100)
    assert inst4.encrypt('Hello, World!') == ',IPPS\x10\x04;SVPH\x05'
    assert inst4.decrypt(',IPPS\x10\x04;SVPH\x05') == 'Hello, World!'

    inst5 = cipher_engine.CaesarCipher(key=3000)
    test = inst5.encrypt('Hello, World!')
    inst5.decrypt(test) == 'Hello, World!'


def test_cipher_hacker():
    plaintext = 'hello world'
    inst = cipher_engine.CaesarCipher(key=5)
    ciphertext = inst.encrypt(plaintext)

    cipher_hacker(plaintext, ciphertext)

    
