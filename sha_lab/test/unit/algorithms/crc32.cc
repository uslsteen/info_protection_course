#include "algorithms/crc32.hh"
#include "test_header.hh"

TEST(algorithms, crc32) {
  CRC32 crc32;
  ASSERT_EQ(crc32(""), "00000000");
  ASSERT_EQ(crc32("hello world"), "0d4a1185");
  ASSERT_EQ(crc32("happy new year"), "be507b68");
}

#include "test_footer.hh"
