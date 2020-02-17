import argparse
import fileinput

from csv2tabulate.converter import convert
from tabulate import _table_formats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "files",
        metavar="FILE",
        nargs="*",
        help="files to read, if empty, stdin is used",
    )
    parser.add_argument(
        "-o", "--output", type=argparse.FileType("w"), default="-"
    )
    parser.add_argument(
        "-f", "--format", choices=_table_formats.keys(), default="github"
    )
    args = parser.parse_args()
    file_objs = fileinput.input(files=args.files)
    table = convert(file_objs, tablefmt=args.format)
    args.output.write(table)


if __name__ == "__main__":
    main()
