#include "algorithms/sha1.hh"
#include "test_header.hh"

TEST(algorithms, 1) {
  SHA1 sha1;
  ASSERT_EQ(sha1(""), "da39a3ee5e6b4b0d3255bfef95601890afd80709");
}

#include "test_footer.hh"