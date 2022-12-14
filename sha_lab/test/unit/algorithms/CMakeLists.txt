set(TARGETS sha1 sha256 sha3 md5 crc32 keccak)
#
foreach(TARGET ${TARGETS})
    #
    set(TAR_NAME ${TARGET}_test)
    add_executable(${TAR_NAME} ${TARGET}.cc)
    upd_tar_list(${TAR_NAME} TESTLIST)

    target_include_directories(${TARGET}
        PRIVATE "${CMAKE_SOURCE_DIR}/include/algorithms/"
    )
endforeach()
