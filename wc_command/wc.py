import argparse
from os.path import getsize
from sys import exit


def filename_from_args(args) -> str:
    if args.file:
        return args.file[0]
    if args.c is not None:
        return args.c
    if args.l is not None:
        return args.l
    if args.w is not None:
        return args.w
    if args.L is not None:
        return args.L

    exit("No file given")


def command_handler(args: argparse.Namespace):
    filename = filename_from_args(args)

    if args.file:
        args.c = filename
        args.l = filename
        args.w = filename

    out = ""
    if args.c is not None:
        out += f" {str(getsize(filename))}"
    if args.l is not None:
        with open(args.l, "r", encoding="utf8") as f:
            out += f" {len(f.readlines())}"
    if args.w is not None:
        with open(args.w, "r", encoding="utf8") as f:
            out += f" {len(f.read().split())}"
    if args.L is not None:
        with open(args.L, "r", encoding="utf8") as f:
            longest = max(f.readlines(), key=len)
            out += f" {len(longest)}"

    out += f" {filename}"
    print(out)


def main():
    parser = argparse.ArgumentParser(description="CW Command")

    parser.add_argument("file", nargs="*")
    parser.add_argument("-c", required=False, help="Give bytezise of file")
    parser.add_argument("-l", required=False, help="Give line count of file")
    parser.add_argument("-w", required=False, help="Give word count of file")
    parser.add_argument(
        "-L", required=False, help="Give length of longest line of file"
    )

    args = parser.parse_args()
    command_handler(args)


if __name__ == "__main__":
    main()
