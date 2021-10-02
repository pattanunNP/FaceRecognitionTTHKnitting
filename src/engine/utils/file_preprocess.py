import time
import os
import shutil
from hashlib import sha256

class file_preprocess:

    @staticmethod
    def generate_hash(Filename:str):
        block_size = 65536
        Filehash = sha256()
        try:
            with open(Filename, 'rb') as File:
                fileblock = File.read(block_size)
                while len(fileblock)>0:
                    Filehash.update(fileblock)
                    fileblock = File.read(block_size)
                Filehash = Filehash.hexdigest()
            return Filehash
        except Exception as err:
            print(err)
            return False

    @staticmethod
    def compare(hash1:str, hash2:str)-> bool:
        if hash1 == hash2:
            return True
        else:
            return False

 
