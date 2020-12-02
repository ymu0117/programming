from programming.cipher.cipher_hacker import transposition_arr_hacking
from programming.cipher.word import load_dictionary, load_Webster
from programming.cipher.cipher_engine import TranspositionCipherArr
from random import choice
from string import ascii_lowercase
from cipher.utils import convert_2d_list, transpose_2d_list 


def test_convert_2d_list():
    plaintxt = 'abcdefghijklmnopqrstuvwxyz'
    key = 3
    my_list = list(bytes(plaintxt, encoding='utf-8', errors='strict'))
    two_d_list = convert_2d_list(my_list, key, 'null')
    assert two_d_list[0] == [97, 98, 99]
    assert two_d_list[-1] == [121, 122, 'null'] 


def test_transpose_2d_list():
    plaintxt = 'abcdefghijklmnopqrstuvwxyz'
    key = 3
    my_list = list(bytes(plaintxt, encoding='utf-8', errors='strict'))
    two_d_list = convert_2d_list(my_list, key, 'null')
    transposed_list = transpose_2d_list(two_d_list)
    assert transposed_list[0] == [97, 100, 103, 106, 109, 112, 115, 118, 121]


def test_transposition_arr():
    plaintxt = 'abcdefghijklmnopqrstuvwxyz'
    key = (3, 'new_york') 
    inst = TranspositionCipherArr(key=key)
    cipher_bytes = inst.encrypt(plaintxt)
    decrypted_str = inst.decrypt(cipher_bytes)
    assert plaintxt == decrypted_str 


def test_transposition_arr_paragraph():
    plaintext = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
                 "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
                 "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
                 "except the key, is public knowledge.")
    key = (4, 'new_york')
    inst = TranspositionCipherArr(key=key)
    cipher_bytes = inst.encrypt(plaintext)
    decrypted_str = inst.decrypt(cipher_bytes)
    assert plaintext == decrypted_str

    
def test_transposition_arr_hacking():
    plaintext = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
                 "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
                 "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
                 "except the key, is public knowledge.")
    key = (29, ''.join(choice(ascii_lowercase) for i in range(29)))
    inst = TranspositionCipherArr(key=key)
    cipher_bytes = inst.encrypt(plaintext)

    path = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.json'
    dictionary = load_Webster(path)

    found_key = transposition_arr_hacking(cipher_bytes, dictionary, percent=0.5) 
    assert found_key == key[0]
  
