import string
import random

class Cipher:
    def __init__(self):
        self.alphabet = string.ascii_uppercase
        self.shift = random.randint(1,25)
        self.cipher = self.create_cipher()

    def create_cipher(self):
        cipher = self.alphabet[self.shift:]
        i = 0
        while len(cipher) < 26:
            cipher += self.alphabet[i]
            i += 1
        return cipher

    def encrypt(self, sentence=None):
        sentence = sentence.upper()
        encryption_dict = {}
        for i,v in enumerate(self.alphabet):
            encryption_dict[ self.alphabet[i] ] = self.cipher[i]
        mapping_table = sentence.maketrans(encryption_dict)
        returned_sentence = sentence.translate(mapping_table)
        return returned_sentence
