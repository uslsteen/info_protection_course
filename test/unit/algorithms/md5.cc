#include "algorithms/md5.hh"
#include "test_header.hh"

TEST(algorithms, md5) {
  MD5 md5;
  ASSERT_EQ(md5(""), "d41d8cd98f00b204e9800998ecf8427e");
}

#include "test_footer.hh"