# put your code here.
from sys import argv

def get_word_count(filename):
    word_count = {}
    with open(filename) as textfile:
        for line in textfile:
            line = line.rstrip()
            words = line.split(" ")
            for word in words:
                word = word.strip(",.?!;:\"").lower()
                word_count[word] = word_count.get(word, 0) + 1
    for key, value in word_count.iteritems():
        print key, value
    return word_count

get_word_count(argv[1])
# get_word_count("twain.txt")
