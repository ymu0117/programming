from cipher.cipher_engine import SubstitutionCipher
from cipher.cipher_hacker import SubstitutionHacker 
from string import ascii_letters, ascii_uppercase, ascii_lowercase
import random 
from cipher.word import load_Webster, load_dictionary
import pickle
from os import path 


def test_substitution():
    random.seed(123) 
    alphabet = ascii_lowercase
    substitution = ''.join(random.sample(alphabet, len(alphabet))) 
    key = dict(zip(alphabet, substitution))
    
    plaintxt = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
                "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
                "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
                "except the key, is public knowledge.")

    inst = SubstitutionCipher(key)
    ciphertxt = inst.encrypt(plaintxt) 
    decrypted_txt = inst.decrypt(ciphertxt) 
    assert plaintxt == decrypted_txt 


def test_substitution_hacker():
    random.seed(123)
    alphabet = ascii_lowercase
    plaintxt = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
                "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
                "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
                "except the key, is public knowledge.")
    inst = SubstitutionCipher.from_alphabet(alphabet)
    ciphertxt = inst.encrypt(plaintxt)
    
    infile = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
    dictionary = load_dictionary(infile)

    inst = SubstitutionHacker(case_type='insensitive', alphabet=alphabet)
    
    result = inst.hacking(ciphertxt, dictionary)
    print(result.hacked_txt) 
