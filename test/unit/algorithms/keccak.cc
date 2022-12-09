#include "algorithms/keccak.hh"
#include "test_header.hh"

TEST(algorithms, keccak) {
  Keccak keccak(Keccak::Keccak224);
  ASSERT_EQ(keccak(""),
            "f71837502ba8e10837bdd8d365adb85591895602fc552b48b7390abd");
}

#include "test_footer.hh"