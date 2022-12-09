#include "algorithms/sha3.hh"
#include "test_header.hh"

TEST(algorithms, sha3) {
  SHA3 sha3;
  ASSERT_EQ(sha3(""),
            "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a");
}
            
#include "test_footer.hh"