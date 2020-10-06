import pytest
from sans_program_project.crypto import ReverseCipher, ReverseCipherByte, CaesarCipher


def test_ReverseCipher():
    plaintext = 'hello world'
    assert ReverseCipher.encrypt(plaintext) == 'dlrow olleh'

    assert ReverseCipherByte.encrypt(plaintext) == b'dlrow olleh'

    inst = CaesarCipher(shift=3)

    assert inst.encrypt('abyz') == 'debc'

    assert inst.decrypt('debc') == 'abyz'

