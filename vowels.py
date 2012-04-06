#!/usr/bin/env python
"""
vowels

Input a list of names as strings.
Generate all possibile alternate versions of that string performing vowel substitution.
Return a list of generated name versions.
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


def generate_name_variations(name):
    temp_vowel_index = get_vowel_index(name.lower())
    if temp_vowel_index.__len__() != 0:
        temp_name_list = [ name.lower() ]
        for current_vowel in temp_vowel_index:
            temp_name_list = get_name_list(temp_vowel_index, temp_name_list)
        print "Completed \"%s\": Total number of names generated: %d" % (name, len(temp_name_list))
        return temp_name_list


def name_hopper(big_list):
    full_list = []
    for current_name in big_list:
        full_list.append( generate_name_variations(current_name) )
    unwrapped_list = []
    for x in full_list:
        print "Length of x:", len(x)
        for y in x:
            unwrapped_list.append(y)
    print "Unwrapped list site: ", len(unwrapped_list)
    f = open("unwrapped_list.txt", "w")
    for z in unwrapped_list:
        f.write(z + "\n")
    f.close()

name_hopper( ["Abdi","Abdul","Abdullahi","Adega","Akinyemi","Amir","Aroni","Bahraini","Bijal","Boit","Boris","Detai","Eegan","Farah","Fatuma","Gacheru","Gandii","Mahindra","Joram","Kabul","Karri","Karua","Kawhaja","Kimani","Kipchogi","Kofi","Kwach","Machozi","Mbaabu","Muchiri","Mugambi","Nyandarua","Okeyo","Olomide","Osire","Rehal"] )
