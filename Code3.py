import argparse

# create argument parser
parser = argparse.ArgumentParser(description="List all words in a file separated by spaces")

# add input file argument
parser.add_argument("input_file", help="Path to input file")

# add output file argument
parser.add_argument("output_file", help="Path to output file")

# parse command line arguments
args = parser.parse_args()

# read in input file
with open(args.input_file, "r") as f:
    # read all lines of the file and join them into one string
    text = "".join(f.readlines())

# split text into words
words = text.split()

# write words to output file
with open(args.output_file, "w") as f:
    f.write(" ".join(words))
