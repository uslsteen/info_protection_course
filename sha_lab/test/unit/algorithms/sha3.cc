#include "algorithms/sha3.hh"
#include "test_header.hh"

TEST(algorithms, sha3_224) {
  SHA3 sha3(SHA3::Bits224);
  ASSERT_EQ(sha3(""),
            "6b4e03423667dbb73b6e15454f0eb1abd4597f9a1b078e3f5b5a6bc7");
  
}
            
TEST(algorithms, sha3_256) {
  SHA3 sha3(SHA3::Bits256);
  ASSERT_EQ(sha3(""),
            "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a");
  
}

TEST(algorithms, sha3_384) {
  SHA3 sha3(SHA3::Bits384);
  ASSERT_EQ(sha3(""),
            "0c63a75b845e4f7d01107d852e4c2485c51a50aaaa94fc61995e71bbee983a2ac3713831264adb47fb6bd1e058d5f004");
  
}


TEST(algorithms, sha3_512) {
  SHA3 sha3(SHA3::Bits512);
  ASSERT_EQ(sha3(""),
            "a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26");
  
}
        
#include "test_footer.hh"