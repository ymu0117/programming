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

    # inst.gen_keys()
    password = '2M8BJi^#'

    assert inst.encrypt('Hello, World!', password) == 'Khoor, Zruog!'

    inst = CaesarCipherGeneric(shift=20)

    assert inst.encrypt('Hello, World!', password) == 'Byffi, Qilfx!'

    inst = CaesarCipherGeneric(shift=46)

    assert inst.encrypt('Hello, World!', password) == 'Byffi, Qilfx!'

    assert inst.decrypt('Byffi, Qilfx!', password) == 'Hello, World!'

