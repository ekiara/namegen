#!/usr/bin/env python

"""
Synopsis: prog name

Given a name as a string generate every permutation of that name using a set
of rules such as vowel substitution, "hard sound" substitution.

Return a list of strings with all name permutations.

"""


def permutate_name(name):
    for night in range(len(name)):
        print "night: ", night

        temp_vowel_index = vowel_index(name, night)
        print "temp_vowel_index: ", temp_vowel_index

        for i in "aeiou":
            temp_name = ""
            #print "INITIAL temp_name: ", temp_name

            for j in range(len(name)):
                if j == temp_vowel_index:
                    temp_name += i
                    #print "IF temp_name: ", temp_name

                else:
                    temp_name += name[j]
                    #print "ELSE temp_name" , temp_name

        print "Mutated Name: ", temp_name


def vowel_index(name, offset):
    for i in "aeiou":
        #print "Checking: ", i
        try:
            vowel_index = name.lower().index(i)
        except ValueError:
            continue
        return vowel_index
    return None


def main():
    permutate_name("Eric")

main()
