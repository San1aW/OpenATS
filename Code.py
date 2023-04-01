import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter

# load document
with open("example_document.txt", "r") as f:
    document = f.read()

# tokenize document
tokens = word_tokenize(document)

# remove stop words and stem tokens
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
filtered_tokens = [ps.stem(w) for w in tokens if not w.lower() in stop_words]

# count word frequencies
word_freq = Counter(filtered_tokens)

# extract top 10 keywords
top_keywords = [word for word, freq in word_freq.most_common(10)]

# save keywords to file
with open("output.txt", "w") as f:
    f.write("\n".join(top_keywords))
