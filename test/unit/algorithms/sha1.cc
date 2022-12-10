#include "algorithms/sha1.hh"
#include "test_header.hh"

TEST(algorithms, 1) {
  SHA1 sha1;
  ASSERT_EQ(sha1(""), "da39a3ee5e6b4b0d3255bfef95601890afd80709");
  ASSERT_EQ(sha1("hello world"), "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed");
}

#include "test_footer.hh"