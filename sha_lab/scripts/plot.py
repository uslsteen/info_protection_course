#!/usr/bin/python3

from pathlib import Path
import argparse
import matplotlib.pyplot as plt
import csv


def parse(path_to_csv: Path) -> dict:
    data = dict()
    #
    with open(path_to_csv, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",")
        #
        for row in spamreader:
            data[row[0]] = int(row[1])
    #
    return data
    #


#
def get_plot(data: dict, title):
    plt.figure(figsize=(16, 10))
    plt.bar(list(data.keys()), data.values(), color="g")
    plt.title(title)
    plt.show()
    #


#
TYPES = ["collisions", "time"]


def main():
    parser = argparse.ArgumentParser(description="Tool to make plots")
    parser.add_argument(
        "--path-to-csv", type=Path, required=True, help="Path to .csv sources"
    )
    parser.add_argument("--type", choices=TYPES, required=True, help="collisions/time")
    #
    args = parser.parse_args()
    #
    exec_path = Path(__file__).resolve().parent
    src_path = exec_path / args.path_to_csv
    plot_type = args.type

    title = "collisions statistics in birthday benchmark"
    if plot_type == "time":
        title = "Time statistics, miliseconds"

    data = parse(src_path)
    #
    get_plot(data, title)
    #


#
if __name__ == "__main__":
    main()
