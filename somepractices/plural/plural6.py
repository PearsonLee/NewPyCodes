# -*- coding: utf-8 -*-

import re
import string


def rules(language='en'):
    for line in open('rules.%s' % language):
        pattern, search, replace = line.split()
        yield lambda word: re.search(pattern, word) and re.sub(search, replace,
                                                               word)


def plural(noun, language='en'):
    for applyRule in rules(language):
        result = applyRule(noun)
        if result:
            return result
