import argparse
import os
from src.main import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="solve n x n singles puzzle(s)")

    parser.add_argument(
        "-d", "--dirname",
        type=str,
        required=True,
        help="Directory in which all .singles files will be read. Will also read sub-directories."
    )

    args = parser.parse_args()

    directory_name = args.dirname

    for root, dirs, files in os.walk(directory_name):
        for file in files:
            if file.endswith(".singles"):
                main(root, file)
