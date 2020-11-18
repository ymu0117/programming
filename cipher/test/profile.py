from programming.cipher.cipher_engine import TranspositionCipher 
from programming.cipher.cipher_engine import TranspositionCipherArr
import time


def main():
    plaintext = ("Kerckhoffs principle is one of the basic principles of modern cryptography. "
                 "It was formulated in the end of the nineteenth century by Dutch cryptographer Auguste Kerckhoffs. "
                 "The principle goes as follows: A cryptographic system should be secure even if everything about the system, "
                 "except the key, is public knowledge.")

    key = 20
    tic1 = time.time()
    inst1 = TranspositionCipher(key)
    cipherbytes1 = inst1.encrypt(plaintext)
    toc1 = time.time()
    print("Elapsed time for Transposition Cipher encrypt is: %.4f" % (toc1-tic1))

    tic2 = time.time() 
    inst2 = TranspositionCipherArr(key=key)
    cipherbytes2 = inst2.encrypt(plaintext)
    toc2 = time.time()
    print("Elapsed time for Transposition Cipher arr encrypt is: %.4f" % (toc2-tic2))

    tic3 = time.time()
    decrypted_str1 = inst1.decrypt(cipherbytes1)
    toc3 = time.time()
    print("Elapsed time for Transposition Cipher decrypt is: %.4f" % (toc3-tic3))

    tic4 = time.time()
    decrypted_str2 = inst2.decrypt(cipherbytes2)
    toc4 = time.time()
    print("Elapsed time for Transposition Cipher decrypt is: %.4f" % (toc4-tic4))


if __name__ == '__main__':
    main() 
