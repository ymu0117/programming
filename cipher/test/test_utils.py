from cipher.utils import  word2pattern, create_pattern_map, \
    simple_extract_words, compile_extract_words, \
    word2table, get_intersected_table, get_solved_mapping, convert_txt
from cipher.word import load_Webster, load_dictionary
from string import ascii_lowercase
from cipher.cipher_engine import SubstitutionCipher
import random 


def test_extract_pattern_map():
    word = 'abandon'
    pattern = word2pattern(word, 'insensitive')
    assert pattern == '0.1.0.2.3.4.2'


def test_extract_pattern_insensitive():
    word = 'Abandon'
    pattern = word2pattern(word, 'insensitive')
    assert pattern == '0.1.0.2.3.4.2'


def test_extract_pattern_sensitive():
    word = 'Abandon'
    pattern = word2pattern(word, 'sensitive')
    assert pattern == '0.1.2.3.4.5.3'
    

def test_create_pattern_map():
    infile = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
    dictionary = load_dictionary(infile)
    pattern_map = create_pattern_map(dictionary, 'insensitive') 
    print(pattern_map) 


def test_create_table():
    word = 'secure'
    infile = '/Users/yumu/Desktop/programming/programming/cipher/dictionary.yaml'
    dictionary = load_dictionary(infile)
    pattern_map = create_pattern_map(dictionary, 'insensitive')
    table = word2table(word, pattern_map, 'insensitive', ascii_lowercase) 
    print(table) 


def test_get_table_intersection():
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

    pattern_map = create_pattern_map(dictionary, 'insensitive')
    words = simple_extract_words(ciphertxt)
    tables = []
    for w in words:
        table = word2table(w, pattern_map, 'insensitive', alphabet)
        tables.append(table)

    intersected_table = get_intersected_table(alphabet, tables)

    solved_mapping, unsolved_mapping = get_solved_mapping(intersected_table) 

    decrypted_txt = convert_txt(ciphertxt, solved_mapping)

