import argparse

# create argument parser
parser = argparse.ArgumentParser(description="Extract words from a text file")

# add input file argument
parser.add_argument("input_file", help="Path to input file")

# add output file argument
parser.add_argument("output_file", help="Path to output file")

# parse command line arguments
args = parser.parse_args()

# read in file and convert all text to lowercase
with open(args.input_file, "r") as f:
    text = f.read().lower()

# remove all special characters and split text into words
words = [word for word in text if word.isalnum() or word.isspace()]
words = "".join(words).split()

# remove conjunctions, prepositions, and helping verbs from the list of words
conjunctions = ["and", "or", "but", "if", "then", "else", "when", "where", "that", "this", "these", "those", "not"]
prepositions = ["with", "at", "from", "into", "during", "including", "until", "against", "among", "throughout", "despite", "towards", "upon", "concerning", "of", "to", "in", "for", "on", "by", "with", "about", "like", "through", "over", "before", "between", "after", "since", "without", "under", "within", "along", "following", "across", "behind", "beyond", "plus", "except", "but", "up", "out", "around", "down", "off", "above", "near"]
helping_verbs = ["am", "is", "are", "was", "were", "be", "being", "been", "have", "has", "had", "do", "does", "did", "will", "shall", "should", "would", "may", "might", "must", "can", "could"]
words = [word for word in words if word not in conjunctions and word not in prepositions and word not in helping_verbs]

# remove duplicates from the list of words
words = list(set(words))

# write the words to the output file
with open(args.output_file, "w") as f:
    f.write(" ".join(words))

# print out the list of words in a grid format
n = len(words)
m = (n + 2) // 3  # calculate number of rows
for i in range(m):
    row = [words[j] if j < n else "" for j in range(i, n, m)]
    num_cols = min(len(row), 3)
    format_str = "".join(["{:<20}"] * num_cols)
    print(format_str.format(*row[:num_cols]))
