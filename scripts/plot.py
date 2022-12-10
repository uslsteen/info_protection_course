#!/usr/bin/python3

from pathlib import Path
import argparse
import matplotlib.pyplot as plt
import csv

def parse(path_to_csv : Path) -> dict:
    data = dict()
    #
    with open(path_to_csv, newline='') as csvfile:
        spamreader  = csv.reader(csvfile, delimiter = ',')
        #
        for row in spamreader:
            data[row[0]] = row[1]
    #
    return data
    #
#
def get_plot(data : dict):
    plt.figure(figsize=(16,10))
    plt.bar(list(data.keys()), data.values(), color ='g')
    plt.title("Time statistics, miliseconds")
    plt.show()
    #
#
def main():
    parser = argparse.ArgumentParser(description="Tool to make plots")
    parser.add_argument("--path_to_csv", type=str, help="Path to .csv sources")
    #
    args = parser.parse_args()
    #
    exec_path = Path.resolve(Path(__file__)).parent
    src_path = exec_path.joinpath(args.path_to_csv)
    data = parse(src_path)
    #
    get_plot(data)
    #
#
if __name__ == "__main__":
    main()