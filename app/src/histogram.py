import re
import string

def get_words(source_text):
    text = open(source_text)
    story = text.read()
    text.close()

    # regex help https://stackoverflow.com/a/13184791/12049271
    delimiters = ' ', '\n'
    regexPattern = '|'.join(map(re.escape, delimiters))
    words = re.split(regexPattern, story)
    words = list(filter(None, [word.strip(string.punctuation).lower() for word in words]))
    return words

def histogram_dict(words):
    histogram = {}
    for word in words:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram

def histogram_list(words):
    histogram = []
    in_list = False

    for word in words:
        for w in histogram:
            if word == w[0]:
                in_list = True
                w[1] += 1
        if in_list == False:
            histogram.append([word, 1])

    return histogram

def histogram_tuple(words):
    histogram = []
    in_tuple = False

    for word in words:
        for w in histogram:
            if word == w[0]:
                in_tuple = True
                histogram.append((word, w[1]+1))
                histogram.remove(w)
        if in_tuple == False:
            histogram.append((word, 1))
        # print(count, histogram)
        # print(count)
        
    return histogram

def unique_words(histogram):
    return len(histogram.keys())

    # low-level attempt
    # count = 0
    # for word in histogram:
    #     count += 1
    
    # return count

def frequency(word, histogram):
    return histogram[word]

if __name__ == "__main__":
    words = get_words('test.txt')
    hist_dict = histogram_dict(words)
    # print(histogram_list(words))
    print(histogram_tuple(words))
    # print(unique_words(hist))
    # print(frequency('hi', hist))
    # print(hist)
