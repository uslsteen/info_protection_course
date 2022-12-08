import hashlib
from pathlib import Path
from collections import defaultdict
from time import time

import seaborn as sns
import matplotlib.pyplot as plt


class SHAWrapper():
    def __init__(self, path : Path, sha_size : int = None, sha_types : str = None) -> None:
        self.path = path
        self.sha_size = sha_size
        self.sha_types = sha_types
        self.data = list()
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
                        tuple([hashlib.blake2b, "blake2b"])]),            \
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
            func, name = cur_sha[0], cur_sha[1]
            self.run_test(func, name)        
        #
    #
    def parse(self):
        with open(self.path) as src:
            pwds = src.read().split('\n')
            for pwd in pwds:
                self.data.append(pwd)
        #
    #
    def run_test(self, func, name : str):
        collisions = defaultdict()
        collisions = defaultdict(lambda:0, collisions)
        #
        print(name)
        start = time()
        for data_it in self.data:
            res_hash = func(data_it.encode())
            if name in ["shake_128", "shake_256"]:
                collisions[res_hash.hexdigest(self.sha_size)] += 1
            else: 
                collisions[res_hash.hexdigest()] += 1
        #
        end = time()
        #
        self.process_collisions(collisions, name)
        # NOTE: miliseconds measurement
        self.time_stats[name] = (end - start) * 1000
        #
    #
    def process_collisions(self, data : defaultdict, name : str):
    #
        collisions_num = 0
        for it in data.values():
            collisions_num += (it - 1)
            #
        self.collisions_stats[name] = collisions_num
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
