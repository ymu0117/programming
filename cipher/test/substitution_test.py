from cipher.cipher_engine import SubstitutionCipher
from cipher.cipher_hacker import substitution_hacking  
from string import ascii_letters, ascii_uppercase, ascii_lowercase
import random 
from cipher.word import load_Webster, load_dictionary


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


# def test_substitution_hacker():
#     random.seed(123)
#     plaintxt = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
#                 "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
#                 "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
#                 "except the key, is public knowledge.")
#     inst = SubstitutionCipher.from_alphabet(ascii_lowercase)
#     ciphertxt = inst.encrypt(plaintxt)
#     
#     infile = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
#     dictionary = load_dictionary(infile)
#     inst = SubstitutionHacker(case_type='insensitive', alphabet=ascii_lowercase)
#     result = inst.hacking(ciphertxt, dictionary)
#     print("\n Hacked text is: \n")
#     print(result.hacked_txt) 
# 
# 
# def test_word2pattern():
#     word = 'advance'
#     inst = SubstitutionHacker(case_type='insensitive', alphabet=ascii_lowercase)
#     pattern = inst.word2pattern(word)
#     assert pattern == '0.1.2.0.3.4.5'
# 
# 
# def test_create_pattern_map():
#     infile = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
#     dictionary = load_dictionary(infile)
#     inst = SubstitutionHacker(case_type='insensitive', alphabet=ascii_lowercase)
#     pattern_map = inst.create_pattern_map(dictionary)
#     print("\n Pattern map is: \n")
#     print(pattern_map) 
# 
#     
# def test_txt2words():
#     plaintxt = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
#                 "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
#                 "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
#                 "except the key, is public knowledge.")
# 
#     words = SubstitutionHacker(case_type='insensitive', alphabet=ascii_lowercase).txt2words(plaintxt)
#     print("\n Converting text to words: \n")
#     print(words)
# 
# 
# def test_word2table():
#     infile = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
#     dictionary = load_dictionary(infile)
#     inst = SubstitutionHacker(case_type='insensitive', alphabet=ascii_lowercase)
#     pattern_map = inst.create_pattern_map(dictionary)
#     word = 'is'
#     table = inst.word2table(word, pattern_map) 
#     print("\n Generating matching table for word {} \n".format(word))
#     print(table)
# 
# 
# def test_get_intersected_table():
#     table1 = {letter: [] for letter in ascii_lowercase}
#     table2 = {letter: [] for letter in ascii_lowercase}
#     table3 = {letter: [] for letter in ascii_lowercase}
# 
#     table1['a'] = ['e', 'f', 'g', 'h']
#     table2['a'] = ['e', 'f']
#     table3['a'] = ['f', 'x', 'z']
# 
#     inst = SubstitutionHacker(case_type='insensitive', alphabet=ascii_lowercase)
#     intersected_table = inst.get_intersected_table([table1, table2, table3])
#     assert intersected_table['a'] == ['f']


def test_hacker(): 
    random.seed(123)
    plaintxt = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
                "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
                "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
                "except the key, is public knowledge.")
    inst = SubstitutionCipher.from_alphabet(ascii_lowercase)
    ciphertxt = inst.encrypt(plaintxt)
    
    infile = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
    dictionary = load_dictionary(infile)

    hacked_txt, solved_mapping, unsolved_mapping = substitution_hacking(ciphertxt, dictionary, 'insensitive', ascii_lowercase)
    print('\n Hacked text is: \n')
    print(hacked_txt)
    print('Solved mapping is: \n')
    print(solved_mapping)
    print('Unsolved mappping is: \n')
    print(unsolved_mapping)

