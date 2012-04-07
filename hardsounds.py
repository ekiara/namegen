#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Given a name, substitute all hardsounds with all variants.

Copyright (c) Eric M. Kiara 2012
"""
HARD_SOUNDS = set(
    ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r",
        "s", "t", "v", "w", "x", "z", "bh", "dh", "gh", "th", "br", "cr",
        "dr", "fr", "gr", "kr", "pr", "sr", "tr", ]
)
SAMPLE_NAMES = set(
    ["mutuma", "abdulla", "eric", "annab", "josphat", "aai", ]
)


def get_consonant_index_positions(name):
    print name
    consonant_index_list = []
    for i in range(len(name)):
        if name[i] in HARD_SOUNDS:
            consonant_index_list.append(i)
    print consonant_index_list


def main():
    """ main
    """
    print HARD_SOUNDS
    print len(HARD_SOUNDS)
    print HARD_SOUNDS.__len__()
    print __name__
    for n in SAMPLE_NAMES:
        get_consonant_index_positions(n)

if __name__ == "__main__":
    main()
