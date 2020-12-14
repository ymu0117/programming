from cipher.cipher_engine import VigenereCipher, _shift_code_points


def test_shift_code_points():
    letter = bytes('a', encoding='utf-8')
    n = 5
    my_byte = _shift_code_points(letter, n)
    assert my_byte == b'f'


def test_encrypt():
    plaintxt = 'Hello, World!'
    key = 'icecream'
    inst = VigenereCipher(key)
    my_bytes = inst.encrypt(plaintxt)
    print(my_bytes)


def test_decrypt():
    plaintxt = 'Hello, World!'
    key = 'icecream'
    inst = VigenereCipher(key)
    my_bytes = inst.encrypt(plaintxt)

    decrypted_txt = inst.decrypt(my_bytes)
    plaintxt == decrypted_txt
