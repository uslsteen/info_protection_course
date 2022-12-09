#include "algorithms/crc32.hh"
#include "test_header.hh"

TEST(algorithms, crc32) {
  CRC32 crc32;
  ASSERT_EQ(crc32(""), "00000000");
}

#include "test_footer.hh"
