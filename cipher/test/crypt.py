import pytest
from sans_program_project.cipher import cipher_engine


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
