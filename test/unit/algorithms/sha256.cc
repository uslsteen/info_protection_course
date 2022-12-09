#include "test_header.hh"
#include "algorithms/sha256.hh"

TEST(algorithms, sha256)
{
    SHA256 sha256;
    ASSERT_EQ(sha256(""), "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855");
}

#include "test_footer.hh"