from pathlib import Path
import argparse
#
from driver import SHAWrapper

def main():
    parser = argparse.ArgumentParser(description="Tool to compare SHA")
    
    parser.add_argument('-p', "--path", type=str, help="Path to password sources directory")
    parser.add_argument('--sha_size', type=int, help="Size of SHA")
    parser.add_argument('--sha_types', type=str, default = [], help="Optional list of SHA types")
    #
    args = parser.parse_args()
    #
    exec_path = Path.resolve(Path(__file__)).parent
    src_path = exec_path.joinpath(args.path)
    #
    driver = SHAWrapper(src_path, args.sha_size, args.sha_types)
    driver.run()
    #
#
if __name__ == "__main__":
    main()