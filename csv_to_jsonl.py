import argparse
import json
import csv


def csv_to_jsonl(input_file, output_file):

    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        with open(output_file, 'w') as jsonfile:
            for row in reader:
                json.dump(row, jsonfile)
                jsonfile.write('\n')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert csv to jsonl")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")

    args = parser.parse_args()

    csv_to_jsonl(args.input_file, args.output_file)
