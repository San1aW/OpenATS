# read in file
with open("filename.txt", "r") as f:
    # read all lines of the file and join them into one string
    text = "".join(f.readlines())

# split text into words
words = text.split()

# print out all the words separated by spaces
print(" ".join(words))
