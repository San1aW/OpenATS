# OpenATS
I am trying to build an open source applicant tracking software. 
This script "codefinal.py' is a Python program that will do following tasks.
1. Extracts words from a text file e.g input.txt
3. Convert all words in lowercase to keep the list unique and avoid repeatation of words
4. Removes all special characters and splits it into a list of words.
5. Removes conjunctions, prepositions, and helping verbs from the list of words. 
6. Finally, the program writes the words to the output file and prints them in a grid format on the console. The grid format consists of rows with a maximum of three columns, and the words are printed left-aligned within each column.

What you need to do:
Copy script to your note editor in linux and save as "extract_words.py" 
Change mode to executable
Then copy a job description and paste it in another text file e.g "input.txt"
Run this syntex on your terminal

python extract_words.py input.txt output.txt


Give any file name you want to save the output. e.g "output.txt"
