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
    words = list(
        filter(None, [word.strip(string.punctuation).lower() for word in words]))
    return words