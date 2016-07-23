# -*- coding: utf-8 -*-

import re


def buildMatchAndApplyFuntion((pattern, search, replace)):
    matchfun = lambda word: re.search(pattern, word)
    applyfun = lambda word: re.sub(search, replace, word)
    return matchfun, applyfun


patterns = (
    ('[sxz]$', '$', 'es'),
    ('[^aeioudgkprt]h$', '$', 'es'),
    ('[^aeiou]y$', 'y$', 'ies'),
    ('$', '$', 's')
)

rules = map(buildMatchAndApplyFuntion, patterns)


def plural(noun):
    for matchf, applyf in rules:
        if matchf(noun):
            return applyf(noun)


if __name__ == '__main__':
    print plural("search")
