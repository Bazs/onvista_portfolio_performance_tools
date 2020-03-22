from argparse import ArgumentParser
import pandas as pd
from pathlib import Path


def convert_onvista_transaction_list_file(input_filename: str):
    wkn_isin_column_headers = "WKN/ISIN"

    transaction_list_frame = pd.read_csv(input_filename, sep=";", skiprows=5)
    wkn_isin_column = transaction_list_frame[wkn_isin_column_headers]
    split_frame = wkn_isin_column.str.split(" / ", expand=True)
    split_frame.columns = ["WKN", "ISIN"]
    transaction_list_frame.drop(columns=[wkn_isin_column_headers])
    transaction_list_frame = pd.concat([transaction_list_frame, split_frame], axis=1)

    input_filename_path = Path(input_filename)
    input_file_folder = input_filename_path.parent
    output_filename = str(input_filename_path.stem) + "_import_ready" + str(input_filename_path.suffix)
    output_filename_path = input_file_folder / output_filename

    transaction_list_frame.to_csv(str(output_filename_path), sep=";", index=False)


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-f", "--file", help="Input file")

    args = arg_parser.parse_args()
    convert_onvista_transaction_list_file(args.file)