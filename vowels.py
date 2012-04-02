#!/usr/bin/env python

"""

"""

from sys import argv

VOWELS = "aeiou"

name = "Eric"

vowel_index = []

name_list = []

for i in range(len(name.lower())):
    if VOWELS.__contains__(name.lower()[i]):
        vowel_index.append(i)

def mutate(name_list):
    for i in vowel_index:
        for j in VOWELS:
            temp_name = name.lower()
            if name_list.__contains__(temp_name) == False:
                name_list.append(temp_name)
    print name_list


