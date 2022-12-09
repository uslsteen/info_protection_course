import random
import argparse

def main():

    parser = argparse.ArgumentParser(description="Tool to compare SHA")

    parser.add_argument('--word_size',"-ws", type=int, help="Input word size (bits)", default = 0)
    parser.add_argument('--data_size', "-ds", type=int, help="Test size of preudo random generated 2 bytes words", default = 0)
    parser.add_argument('-p', "--path", type=str, help="Path to password sources directory", default = None)
    #
    args = parser.parse_args()
    
    data = gen_data(args.data_size, args.word_size)

    dump(args.path ,data)

def dump(path, data : set):
#
    with open(path, 'w') as f:
        for it in data:
            print(it, file=f)
#
def gen_data(size : int, nbits : int = 16) -> list:
#
    data = list()
    for _ in range(size):
        data.append(random.getrandbits(nbits))
    #
    return data
#

if __name__ == "__main__":
    main()