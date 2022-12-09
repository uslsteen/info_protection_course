set(TARGETS sha1 sha256 sha3 md5 crc32 keccak)
#
foreach(TARGET ${TARGETS})
    #
    add_executable(${TARGET} ${TARGET}.cc)
    upd_tar_list(${TARGET} TESTLIST)

    target_include_directories(${TARGET}
        PRIVATE "../../../include/algorithms/"
    )
endforeach()




