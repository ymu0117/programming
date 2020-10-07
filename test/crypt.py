import pytest
from sans_program_project.crypto import ReverseCipher, ReverseCipherByte, CaesarCipher


def test_ReverseCipher():
    plaintext = 'hello world'
    inst = ReverseCipher()
    assert inst.encrypt(plaintext) == 'dlrow olleh'


def test_ReverseCipherBytes():
    plaintext = 'hello world'
    inst = ReverseCipherByte()
    assert inst.encrypt(plaintext) == 'dlrow olleh'


def test_CaesarCipher():
    inst1 = CaesarCipher(key=3)
    assert inst1.encrypt('abcd') == 'defg'
    assert inst1.decrypt('defg') == 'abcd'

    inst2 = CaesarCipher(key=3)
    assert inst2.encrypt('Hello, World!') == 'Khoor/#Zruog$'
    assert inst2.decrypt('Khoor/#Zruog$') == 'Hello, World!'
