from programming.cipher.cipher_engine import SubstitutionCipher
from string import ascii_uppercase, ascii_lowercase
import random 


def test_substitution():
    random.seed(123) 
    alphabet = ascii_uppercase + ascii_lowercase + '0123456789'
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

