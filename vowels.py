#!/usr/bin/env python

"""

"""

from sys import argv

VOWELS = "aeiou"

def get_vowel_index(name):
    vowel_index = []
    for i in range(len(name.lower())):
        if VOWELS.__contains__(name.lower()[i]):
            vowel_index.append(i)
    return vowel_index

def get_name_list(vowel_index, name_list):
    for jina in name_list:
        for i in vowel_index:
            for j in VOWELS:
                temp_name = jina.lower()
                temp_name = temp_name[:i] + j + temp_name[i+1:]
                if name_list.__contains__(temp_name) == False:
                    name_list.append(temp_name)
    return name_list

def main(name):
    vi = get_vowel_index(name.lower())
    nl = [name.lower()]
    print "vowel index is now: %r, and namelist is now: %r" % (vi,nl)
    for i in vi:
        nl = get_name_list(vi, nl)
    print "Completed generating names."
    print nl
    print "Total number of names generated: %d" % len(nl)

main(argv[1])
