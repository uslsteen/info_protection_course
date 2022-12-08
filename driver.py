import hashlib
from pathlib import Path
from collections import defaultdict
from time import time

import matplotlib.pyplot as plt

class SHAWrapper():
    def __init__(self, path : Path = None, sha_size : int = None, sha_types : str = None) -> None:
    #
        self.path = path
        self.sha_size = sha_size
        self.sha_types = sha_types
        self.data = set()
        #
        self._size2algo = dict({
            128 : list([tuple([hashlib.md5, "md5"]),                    \
                        tuple([hashlib.shake_128, "shake_128"]),        \
                        tuple([hashlib.blake2s, "blake2s"]),            \
                        tuple([hashlib.blake2b, "blake2b"])]),          \
            #
            224 : list([tuple([hashlib.sha224, "sha224"]),              \
                        tuple([hashlib.sha3_224, 'sha3_224']),          \
                        tuple([hashlib.blake2s, 'blake2s']),            \
                        tuple([hashlib.blake2b, "blake2b"])]),          \
            #
            256 : list([tuple([hashlib.sha256, 'sha256']),              \
                        tuple([hashlib.sha3_256, "sha3_256"]),          \
                        tuple([hashlib.shake_256, "shake_256"]),        \
                        tuple([hashlib.blake2s, 'blake2s']),            \
                        tuple([hashlib.blake2b, "blake2b"])]),          \
            #
            384 : list([tuple([hashlib.sha384, "sha384"]),              \
                        tuple([hashlib.sha3_384, "sha3_384"]),          \
                        tuple([hashlib.blake2b, "blake2b"])]),          \
            #
            512 : list([tuple([hashlib.sha512, "sha512"]),              \
                        tuple([hashlib.sha3_512, "sha3_512"]),          \
                        tuple([hashlib.blake2b, "blake2b"])]),          \
        })
        #
        self.collisions_stats = dict()
        self.time_stats = dict()
        #
    #
    def get_sha(self, size : int) -> list:
        return self._size2algo.get(size)
        #
    #
    def run(self):
        self.parse()
        cur_shas = self._size2algo.get(self.sha_size)
        #
        for cur_sha in cur_shas:
            hash_func, name = cur_sha[0], cur_sha[1]
            self.run_sha(hash_func, name)        
        #
    #
    def parse(self):
    #
        with open(self.path) as src:
            words = src.read().split('\n')
            for word in words:
                self.data.add(word)
        #
    #
    def run_sha(self, hash_func, name : str):
        hash_set, collisions_num = set(), 0
        hex_hash, hash = None, None
        #
        start = time()
        print(name)

        for data_it in self.data:

            if isinstance(data_it, int):
                data_it = hex(data_it).encode()
            else: data_it = data_it.encode()
            #
            if name in ["blake2b", "blake2s"]:
                hash = hash_func(data_it, digest_size = self.sha_size // 8)
            else:
                hash = hash_func(data_it)
            #
            if name in ["shake_128", "shake_256"]:
                hex_hash = hash.hexdigest(self.sha_size // 8) 
            else: 
                hex_hash = hash.hexdigest()
            #
            if hex_hash in hash_set:
                print(f"data = {data_it}, hex_hash = {hex_hash}")
                collisions_num +=1
            else: hash_set.add(hex_hash)
        #
        end = time()
        #
        # NOTE: miliseconds measurement
        self.collisions_stats[name] = collisions_num
        self.time_stats[name] = (end - start) * 1000
        #
    #
    def get_collisions_stats(self):
        plt.figure(figsize=(16,10))
        plt.bar(list(self.collisions_stats.keys()), self.collisions_stats.values(), color ='g')
        plt.title("Collisions stats")
        plt.show()
        #
    #
    def get_time_stats(self):
        plt.figure(figsize=(16,10))
        plt.bar(list(self.time_stats.keys()), self.time_stats.values(), color ='r')
        plt.title("Time stats")
        plt.show()
        #
    #
#