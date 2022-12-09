add_executable(sha256 sha256.cc)
upd_tar_list(sha256 TESTLIST)

target_include_directories( sha256
    PRIVATE "../../../src/" # TODO: fix
    PRIVATE "../../../src/algorithms/"
)