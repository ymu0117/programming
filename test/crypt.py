import pytest
from sans_program_project.crypto import ReverseCipher, ReverseCipherByte, CaesarCipher, CaesarCipherGeneric


def test_ReverseCipher():
    plaintext = 'hello world'
    assert ReverseCipher.encrypt(plaintext) == 'dlrow olleh'

    assert ReverseCipherByte.encrypt(plaintext) == b'dlrow olleh'

    inst = CaesarCipher(shift=3)

    assert inst.encrypt('abyz') == 'debc'

    assert inst.decrypt('debc') == 'abyz'

    inst = CaesarCipherGeneric(shift=3)

    assert inst.encrypt('Hello, World!') == 'Khoor, Zruog!'

    inst = CaesarCipherGeneric(shift=20)

    assert inst.encrypt('Hello, World!') == 'Byffi, Qilfx!'

    inst = CaesarCipherGeneric(shift=46)

    assert inst.encrypt('Hello, World!') == 'Byffi, Qilfx!'

    assert inst.decrypt('Byffi, Qilfx!') == 'Hello, World!'
