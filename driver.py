import hashlib
from pathlib import Path
from collections import defaultdict
from time import time

class SHAWrapper():
    def __init__(self, path : Path, sha_types : str()) -> None:
        self.path = path
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
                        tuple(hashlib.blake2b, "blake2b")]),            \
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
    def parse(self):
        with open(self.path) as src:
            self.data(src.readline()) 
        #
    #s
    def run_test(self, func, name : str, size : int):
        collisions = defaultdict(lambda:0, collisions)
        #
        start = time()
        for data_it in self.data:
            res_hash = func(data_it)
            collisions[res_hash] += 1
        #
        end = time()
        #
        self.process_collisions(collisions, name, size)
        self.time_stats[tuple([name, size])] = end - start
        #
    #
    def run(self):
        self.parse()

        for (size, cur_shas) in self._size2algo.items():
            for cur_sha in cur_shas:
                func, name = cur_sha[0], cur_sha[1]
                self.run_test(func, name, size)        
        #
    #
    def process_collisions(self, data : defaultdict, name : str, size : int):
    #
        collisions_num = 0
        for it in data.values():
            collisions_num += (it - 1)
            #
        self.collisions_stats[tuple([name, size])] = collisions_num
