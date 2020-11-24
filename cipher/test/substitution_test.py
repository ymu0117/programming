from programming.cipher.cipher_engine import SubstitutionCipher
from programming.cipher.cipher_hacker import substitution_hacking, create_pattern_map  
from string import ascii_letters, ascii_uppercase, ascii_lowercase
import random 
from programming.cipher.word import load_Webster, load_dictionary
import pickle
from os import path 


# def test_substitution():
#     random.seed(123) 
#     alphabet = ascii_lowercase
#     substitution = ''.join(random.sample(alphabet, len(alphabet))) 
#     key = dict(zip(alphabet, substitution))
#     
#     plaintxt = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
#                 "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
#                 "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
#                 "except the key, is public knowledge.")
# 
#     inst = SubstitutionCipher(key)
#     ciphertxt = inst.encrypt(plaintxt) 
#     decrypted_txt = inst.decrypt(ciphertxt) 
#     assert plaintxt == decrypted_txt 
# 
# 
# def test_substitution_hacking():
#     alphabet = ascii_letters
#     substitution = ''.join(random.sample(alphabet, len(alphabet))) 
#     key = dict(zip(alphabet, substitution))
#     plaintxt = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
#                 "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
#                 "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
#                 "except the key, is public knowledge.")
# 
#     inst = SubstitutionCipher(key)
#     ciphertxt = inst.encrypt(plaintxt)
#     
#     percent = 0.5 
#     infile0 = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.json'
#     dictionary = load_Webster(infile0)
# 
#     infile1 = '/Users/yumu/Desktop/programming/programming/cipher/test/pattern_map.pickle'
#     if path.exists(infile1):
#         with open(infile1, 'rb') as f:
#             pattern_map = pickle.load(f)
#     else: 
#         pattern_map = create_pattern_map(dictionary)
#         with open('pattern_map.pickle', 'wb') as f:
#             pickle.dump(pattern_map, f, protocol=pickle.HIGHEST_PROTOCOL) 
# 
#     substitution_hacking(ciphertxt, pattern_map,  percent) 
#     print("done")
# 

def test_substitution_hacking_simple():
    # alphabet = ascii_letters
    random.seed(123) 
    alphabet = ascii_lowercase 
    substitution = ''.join(random.sample(alphabet, len(alphabet))) 
    key = dict(zip(alphabet, substitution))
    plaintxt = ("If a man is offer a fact which go against his instinct, he will scrutinize it closely, and unless "
    "the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offer something which afford a reason "
    "for acting in accordance to his instinct, he will accept it even on the slight evidence. The origin of myth is explain "
    "in this way.")
    inst = SubstitutionCipher(key)
    ciphertxt = inst.encrypt(plaintxt)
    percent = 0.5
    
    infile0 = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.json'
    dictionary = load_Webster(infile0)
#     infile2 = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
    # dictionary = load_dictionary(infile2)

    pattern_map = create_pattern_map(dictionary) 

    infile1 = '/Users/yumu/Desktop/programming/programming/cipher/test/pattern_map.pickle'
    # if path.exists(infile1):
    #     with open(infile1, 'rb') as f:
    #         pattern_map = pickle.load(f)
    # else: 
    #     pattern_map = create_pattern_map(dictionary)
    #     with open('pattern_map.pickle', 'wb') as f:
    #         pickle.dump(pattern_map, f, protocol=pickle.HIGHEST_PROTOCOL) 
    
    decrypted_txt = substitution_hacking(ciphertxt, pattern_map, percent) 

    print("done") 
