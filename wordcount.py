# put your code here.


def get_word_count(filename):
    word_count = {}
    with open(filename) as textfile:
        for line in textfile:
            line = line.rstrip()
            words = line.split(" ")
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    for key, value in word_count.iteritems():
        print key, value
    return word_count

# get_word_count("test.txt")
get_word_count("twain.txt")
