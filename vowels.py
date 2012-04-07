#!/usr/bin/env python
"""
vowels
Fast generation of name alternatives.
"""
VOWELS = set("aeiou")
sample_name_list = ["Abdi", "Abdul", "Adega", "Amir", "Aroni", "Boit", "Gacheru", "Kabul", "Karri", "Karua", "Kimani", "Kipchogi", "Kofi", "Machozi", "Muchiri", "Mugambi", "Okeyo", "Olomide", "Osire"]


def vowel_count(name):
    """Given a name, return the number of vowels."""
    count = 0
    for i in VOWELS:
        count += name.count(i)
    return count


def name_matrix(name):
    """Generate matrix of names."""
    matrix = []
    for i in range(5**vowel_count(name)):
        matrix.append(name)
    return matrix


def vowel_index(name):
    """Return a list of index positions
    where vowels appear in the name.
    """
    vowel_index = []
    for i in range(len(name)):
        if VOWELS.__contains__(name[i]):
            vowel_index.append(i)
    return vowel_index


def vowel_list(count):
    """Build up a list of vowels.
    """
    vlist = []
    for i in range(count):
        vlist.extend(list(VOWELS))
    return vlist


def mutate(matrix, vowel_list, vowel_index):
    """
    """
    for position in vowel_index:
        matrix.sort()
        for i in range(len(matrix)):
            templist = list(matrix[i])
            templist.__setslice__(position,position+1,vowel_list[i])
            tempstr = ""
            for j in templist:
                tempstr += j
            matrix[i] = tempstr
    return matrix


def main(name_collection):
    unwrapthis = []
    for upper in name_collection:
        name = upper.lower()
        index = vowel_index(name)
        matrix = name_matrix(name)
        vlist = vowel_list( len(matrix) )
        new_matrix = mutate(matrix, vlist, index)
        #print len(new_matrix)
        #print new_matrix
        unwrapthis.extend(new_matrix)
    print "Total unwrapped names is {}".format(len(unwrapthis))
    f = open("other_list.txt", "w")
    for z in unwrapthis:
        f.write(z + "\n")
    f.close()
