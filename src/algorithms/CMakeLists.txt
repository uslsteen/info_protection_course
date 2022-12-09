set(TARGETS sha1 sha256 sha3 md5 crc32 keccak)
add_library(algorithms sha1.cc sha256.cc sha3.cc md5.cc crc32.cc keccak.cc)