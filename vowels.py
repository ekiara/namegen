#!/usr/bin/env python
# vowels

#def sub_vowel(vowel):
    #vowel_list = []
    #alternative_vowel = "a"
    #return alternative_vowel

###
### Specification:
###
### Take a name (a string)
###
### Replace every internal vowel with every alternative vowel:
###   - "internal vowel" means a single character vowel that DOES NOT have the index of 0 or -1
###   - "alternative vowel" is given any vowel, all other vowels that are not that vowel are alternative vowels
###
### Return an array of strings that have every permutation of internal vowel alternatives
###


def alternative_vowel(vowel):
    #alt_vowel_list = ["a","e","i","o","u","y"]
    alt_vowel_list = ["a","e","i","o","u"]

    if (alt_vowel_list.__contains__(vowel)):
        return alt_vowel_list.remove(vowel)
    else:
        return []


def index_a(name):
    index_a = []
    index_position = 0
    try:
        while 1:
            if index_position = -1:
                break
            else:
                if len(index_a) = 0:
                    index_position = name.find("a")
                else:
                    index_position = name.find("a", index_a[-1])
            index_a.append(index_position)
    catch ValueError:
        return
