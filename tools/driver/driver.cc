#include "driver.hh"
#include <CLI/CLI.hpp>

int main(int argc, char **argv) {

  std::string path_to_src{}, output{};
  std::size_t sha_xx = 0;
  std::vector<std::string> sha_names{};

  CLI::App cli_app("Tool to compare SHA");

  cli_app.add_option("--sha_xx", sha_xx, "Trunk size (bits) of SHA")
      ->required();
  //
  cli_app.add_option("--path", path_to_src, "Path to test")
      ->required()
      ->check(CLI::ExistingFile);
  //
  cli_app.add_option("--output", output, "Path to output file")->required();
  //
  CLI11_PARSE(cli_app, argc, argv);
  //
  sha_driver::SHAWrapper wrap{path_to_src, output, sha_xx};
  wrap.run_time();
  wrap.run_collisions();
  wrap.dump();

  return 0;
}