#!/usr/bin/env python3

import pandas as pd
import glob
import os, sys


def fuseCsv():
    files = sys.argv
    combined_data = pd.DataFrame()

    if len(files) == 1:
        print(
            f"""\n[USAGE]: {files[0]} . (to fuse every .csv in current folder)\nor\n{files[0]} <file1.csv> <file2.csv> [OPTIONAL:<etc.csv>]\n"""
        )
    elif len(files) == 2 and files[1] == ".":
        files = glob.glob(f"{os.getcwd()}/*.csv")
        if len(files) == 0:
            print("No .csv files found")

        else:
            print(".csv files found:\n")
            for file in files:
                print(f'{file.split("/")[-1]}')

            fusion_file_name = input(
                "\nWhat should the fused file be named?\n(ps. no need to add .csv)\n\n"
            )

            header_in_file = input("Are there headers in the files? (Y/N) ")

            while header_in_file.lower() != "y" and header_in_file.lower() != "n":
                header_in_file = input(
                    "\nYo! Provide a proper answer!\nAre there headers in the files? (Y/N) "
                )

            if header_in_file.lower() == "y":
                for file in files:
                    df = pd.read_csv(file, header=0)
                    combined_data = pd.concat([combined_data, df], ignore_index=True)
                combined_data.to_csv(
                    f"{os.getcwd()}/{fusion_file_name}.csv", index=False
                )
                print(f"\n{os.getcwd()}/{fusion_file_name}.csv saved!")
                print(combined_data)

            elif header_in_file.lower() == "n":
                for file in files:
                    df = pd.read_csv(file, header=None)
                    combined_data = pd.concat([combined_data, df], ignore_index=True)
                combined_data.to_csv(
                    f"{os.getcwd()}/{fusion_file_name}.csv", index=False
                )
                print(f"\n{os.getcwd()}/{fusion_file_name}.csv saved!")
                print(combined_data)

    elif len(files) == 3:
        files = [f"{os.getcwd()}/{file}" for file in files[1:]]
        print(files)


if __name__ == "__main__":
    fuseCsv()
