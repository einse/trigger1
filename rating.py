# -*- coding: utf-8 -*-

from lexem import lexem_type
from output import output

def print_rating(a, t, tokens_lists, blacklist = set(), rating_limit = 20):
    """Returns three numbers:
1) count of all types of tokens,
2) count of all real words in dictionary,
3) count of 'whitelisted' words."""
    words = {}
    for i, _list in enumerate(tokens_lists):
        for j, token in enumerate(_list):
            if token in words:
                words[token] = words[token] + 1
            else:
                words[token] = 1
    nominees = sorted(words.keys(),
                  key=lambda v: words[v],
                  reverse=True)
    real_words = filter(lambda v: lexem_type(v[0]) == 'L', nominees)
    whitelist = filter(lambda v: v not in blacklist, real_words)
    for i, word in enumerate(whitelist):
        if i >= rating_limit:
            break
        place = i + 1
        output(a, t, u"""{:5} {:5} {}""".format(place, words[word], word))
    return len(words), len(real_words), len(whitelist)
