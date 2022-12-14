#include "algorithms/keccak.hh"
#include "test_header.hh"

TEST(algorithms, keccak224) {
  Keccak keccak(Keccak::Keccak224);
  ASSERT_EQ(keccak(""),
            "f71837502ba8e10837bdd8d365adb85591895602fc552b48b7390abd");

  ASSERT_EQ(keccak("hello world"),
            "25f3ecfebabe99686282f57f5c9e1f18244cfee2813d33f955aae568");
}

TEST(algorithms, keccak256) {
  Keccak keccak(Keccak::Keccak256);
  ASSERT_EQ(keccak(""),
            "c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470");

  ASSERT_EQ(keccak("hello world"),
            "47173285a8d7341e5e972fc677286384f802f8ef42a5ec5f03bbfa254cb01fad");
}

TEST(algorithms, keccak384) {
  Keccak keccak(Keccak::Keccak384);
  ASSERT_EQ(keccak(""),
            "2c23146a63a29acf99e73b88f8c24eaa7dc60aa771780ccc006afbfa8fe2479b2dd2b21362337441ac12b515911957ff");

  ASSERT_EQ(keccak("hello world"),
            "65fc99339a2a40e99d3c40d695b22f278853ca0f925cde4254bcae5e22ece47e6441f91b6568425adc9d95b0072eb49f");
}

TEST(algorithms, keccak512) {
  Keccak keccak(Keccak::Keccak512);
  ASSERT_EQ(keccak(""),
            "0eab42de4c3ceb9235fc91acffe746b29c29a8c366b7c60e4e67c466f36a4304c00fa9caf9d87976ba469bcbe06713b435f091ef2769fb160cdab33d3670680e");

  ASSERT_EQ(keccak("hello world"),
            "3ee2b40047b8060f68c67242175660f4174d0af5c01d47168ec20ed619b0b7c42181f40aa1046f39e2ef9efc6910782a998e0013d172458957957fac9405b67d");
}

#include "test_footer.hh"