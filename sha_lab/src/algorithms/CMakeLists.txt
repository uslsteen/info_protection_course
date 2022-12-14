set(SRCS sha1 sha256 sha3 md5 crc32 keccak)

foreach(SRC ${SRCS})
  add_library(${SRC} ${SRC}.cc)
  list(APPEND LIBLIST ${SRC})
endforeach()

set(LIBLIST "${LIBLIST}" PARENT_SCOPE)
