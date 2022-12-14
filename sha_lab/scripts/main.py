#!/usr/bin/python3

from pathlib import Path
import argparse
#
from driver import SHAWrapper

def main():
    parser = argparse.ArgumentParser(description="Tool to compare SHA")
    
    parser.add_argument('--sha_size', '-ss', type=int, help="Output size (bits) of SHA")
    parser.add_argument('-p', "--path", type=str, help="Path to test")
    parser.add_argument('--sha_types', type=str, help="Optional list of SHA types", default = list())
    #
    args = parser.parse_args()
    #
    exec_path = Path.resolve(Path(__file__)).parent
    src_path = exec_path.joinpath(args.path)
    #
    driver = SHAWrapper(src_path, args.sha_size, args.sha_types)
    #
    driver.run()
    driver.get_time_stats()
    driver.get_collisions_stats()
    #
#
if __name__ == "__main__":
    main()