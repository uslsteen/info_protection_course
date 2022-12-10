#ifndef DRIVER_HH
#define DRIVER_HH

#include <filesystem>
#include <fstream>
#include <functional>
#include <iostream>
#include <string_view>
#include <unordered_map>
#include <vector>
#include <unordered_set>
#include <cmath>
#include <random>
//
#include "algorithms/crc32.hh"
#include "algorithms/keccak.hh"
#include "algorithms/md5.hh"
#include "algorithms/sha1.hh"
#include "algorithms/sha256.hh"
#include "algorithms/sha3.hh"
//
#include "timer/timer.hh"

namespace sha_driver {
class SHAWrapper final {

public:
  template <typename FuncT>
  using map_t = typename std::unordered_map<std::string, FuncT>;

private:
  std::ifstream m_in{};
  std::ofstream m_out{};
  std::vector<std::string> m_sha_names{};
  std::size_t m_sha_xx = 0;
  //
  map_t<std::function<std::string(const std::string &)>> m_sha_impl_map{};
  //
  std::vector<std::string> m_words{};
  //
  std::unordered_map<std::string, double> m_time_stats{};
  std::unordered_map<std::string, std::size_t> m_collisions_stats{};
  //
public:
  SHAWrapper(const std::string &path_to_src, const std::string &output,
             std::size_t sha_xx)
      : m_sha_names({"sha1",
                     //
                     "sha3_224", "sha3_256", "sha3_384", "sha3_512",
                     //
                     "sha256",
                     //
                     "keccak_224", "keccak_256", "keccak_384", "keccak_512",
                     //
                     "MD5"}),
        //
        m_sha_xx(sha_xx)
  //
  {
    initImplMap();
    //
    m_in.open(path_to_src);
    m_out.open(output, std::ofstream::out);
    //
    parse();
  }
  //
  SHAWrapper(const SHAWrapper &) = delete;
  SHAWrapper(SHAWrapper &&) = delete;
  SHAWrapper &operator=(const SHAWrapper &) = delete;
  SHAWrapper &operator=(SHAWrapper &&) = delete;

  ~SHAWrapper() {
    m_in.close();
    m_out.close();
  }

  void initImplMap() {
    SHA1 sha1{};
    m_sha_impl_map.insert(std::make_pair("sha1", sha1));
    //
    SHA3 sha3_224{SHA3::Bits224}, sha3_256{SHA3::Bits256},
        sha3_384{SHA3::Bits384}, sha3_512{SHA3::Bits512};
    //
    m_sha_impl_map.insert(std::make_pair("sha3_224", sha3_224));
    m_sha_impl_map.insert(std::make_pair("sha3_256", sha3_256));
    m_sha_impl_map.insert(std::make_pair("sha3_384", sha3_384));
    m_sha_impl_map.insert(std::make_pair("sha3_512", sha3_512));
    //
    SHA256 sha256{};
    m_sha_impl_map.insert(std::make_pair("sha256", sha256));
    //
    Keccak keccak_224{Keccak::Keccak224}, keccak_256{Keccak::Keccak256},
        keccak_384{Keccak::Keccak384}, keccak_512{Keccak::Keccak512};
    //
    m_sha_impl_map.insert(std::make_pair("keccak_224", keccak_224));
    m_sha_impl_map.insert(std::make_pair("keccak_256", keccak_256));
    m_sha_impl_map.insert(std::make_pair("keccak_384", keccak_384));
    m_sha_impl_map.insert(std::make_pair("keccak_512", keccak_512));
    //
    MD5 md5{};
    m_sha_impl_map.insert(std::make_pair("MD5", md5));
  }

  void parse() {
    if (m_in.is_open()) {
      while (m_in) {
        std::string line{};
        std::getline(m_in, line);
        m_words.push_back(line);
      }
    }
  }

  /**
   * @brief
   *
   */
  void run_time() {
    //
    for (auto &&m_sha_name : m_sha_names) {
      auto &&hash_func = m_sha_impl_map.at(m_sha_name);
      //
      timer::Timer my_time{};
      for (auto &&word : m_words)
        auto hash = hash_func(word);
      //
      auto cur_time = my_time.elapsed<timer::Timer::millisecs>();
      m_time_stats.insert(std::make_pair(m_sha_name, cur_time));
    }
  }

  void run_collisions() {
    std::size_t n = 1000;

    for (auto &&m_sha_name : m_sha_names) {
      m_collisions_stats[m_sha_name] = 0;
    }
    for (std::size_t i = 0; i < n; ++i) {
      for (auto &&m_sha_name : m_sha_names) {
        auto &&hash_func = m_sha_impl_map.at(m_sha_name);
        std::unordered_set<std::string> hashes;
        for(std::size_t j = 0; j < std::pow(2, m_sha_xx / 2); ++j) {
          auto&& random_message = gen_random(78);
          auto&& hash = hash_func(random_message);
          hash.resize(m_sha_xx / 4);
          if (hashes.count(hash)) {
            m_collisions_stats[m_sha_name] += 1;
          } else {
            hashes.insert(hash);
          }
        }
      }
    }
  }

  void dump() {
    for (auto &&it : m_time_stats) {
      m_out << it.first << "," << it.second << std::endl;
    }

    for (auto &&it: m_collisions_stats) {
      std::cout << it.first << "," << it.second << std::endl;
    }
  }

  std::string gen_random(const int len) {
    static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";
    std::string tmp_s;
    tmp_s.reserve(len);

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(0, len - 1);

    for (int i = 0; i < len; ++i) {
        tmp_s += alphanum[distrib(gen) % (sizeof(alphanum) - 1)];
    }
    
    return tmp_s;
}
};
} // namespace sha_driver

#endif //! DRIVER_HH