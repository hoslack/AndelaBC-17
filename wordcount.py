import re
from collections import Counter


def words(sentence):
    result = {}
    if not isinstance(sentence,str):
        raise TypeError
    else:
        words = re.sub('\s+', ' ', sentence)
        words = words.split()
        result = dict((x, words.count(x)) for x in set(words))
        return result
