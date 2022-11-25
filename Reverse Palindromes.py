#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:23:32 2021

@author: Matthew
"""

def substring_gen(string, length):
    chars = list(string)
    substrings = []
    positions = []
    for i in range(len(chars)+1-length):
        substring = ''
        for j in range(i, i+length):
            substring += chars[j]
        substrings.append(substring)
        positions.append(i+1)
    return(substrings, positions)

def generate_all_substrings(string, min_length, max_length):
    all_substrings = []
    all_positions = []
    for i in range(min_length, (max_length+1)):
        substrings, positions = substring_gen(string, i)
        all_substrings.append(substrings)
        all_positions.append(positions)
    return(all_substrings, all_positions)

def is_reverse_palindrome(string):
    chars = list(string)
    dummy = []
    for i in range(len(chars)-1, 0, -1):
        dummy.append(chars[i])
    dummy.append(chars[0])
    base = ['A', 'T', 'G', 'C']
    complementary = ['T', 'A', 'C', 'G']
    final = ''
    for i in range(len(dummy)):
        for j in range(len(base)):
            if dummy[i] == base[j]:
                final += complementary[j]
    if final == string:
        return(True)
    else:
        return(False)
    

def find_reverse_palindromes(string, min_length, max_length):
    all_substrings, all_positions = generate_all_substrings(string, min_length, max_length)
    reverse_palindromes = []
    reverse_palindrome_positions = []
    for i in range(len(all_substrings)):
        for j in range(len(all_substrings[i])):
            if is_reverse_palindrome(all_substrings[i][j]) == True:
                reverse_palindromes.append(all_substrings[i][j])
                reverse_palindrome_positions.append(all_positions[i][j])
    for i in range(len(reverse_palindromes)):
        print(f'{reverse_palindrome_positions[i]} {len(reverse_palindromes[i])}')
    
    
find_reverse_palindromes('TATAGGTTTACCATCTAATTGTGGGAAGCGGTTCGTTTACGGCCCAGCCTTGGCACCATGCAGGACATAATGGGATCGAACGTATGAGACTTAATTACTAAAGTAGAGTTTGGGAGGCCGTGACGCTCCTTACTACAGCGTCTGCTCGGCGGTTTGGACTACGGTGTGGAATTGATGGCTCCGAAATTATTAGGCCGCTATAAGCGACGTGCAATCGGTGGTGAGGCAGAGGGCGCAGACAGTGCGCACCAGAGGGACGTACCTAGTGGCCAAATTGAGGGTCCATTGCGCCATCAGTGTACTGTCCGGAGGCCAAGCTGCGCCTCCGCCGAGATTCATGAACGCATGCGCTGCGGAATTAAATAATGCATCTCAGTGCTCTAGTGGTTGTCCTTCATCGCTGACGGGATCTGCACAAGATGTGTCAGCGTCTGCACTCACGCACGTTTAATAAAGTTGTAGCAGATGGTTGTAGCTCTTGGGCCCGGCGGCTATAGCCGGCTGGTCAGGTTCGTGATGAATGAGCCGCGGACCTGAATGTGCAACATATTAGCGTTACGCTGCAAGGCCCGGTCTTTGTTATTTCTCAACCTGAGTTGGTATGAACCTTCAATATCCAGCTTACTTTTGGGATGCGCCCACGGCTAGCGGTGAGCCCGCCACCACGCAATCGAGGGACCCAGATAAGAATTATACGTAAGTACTCAGCACAGCCGAGATTAACGTCCTGGCGCGAGATATAGACGCACTGCGTGTGCCAAGGAGAATCGCCATTAGCGAGCACAGTGACAGGGGTTCATATTTGAGTCGCACCACCTGTAGCGTATCTTTCTACTTCCCGCGTTGTTTCAATGGGTTACAGAGTAAAACGCGCGGTATCAACCCCGTGACGATGCATCTAAAGTTTAGCTTTCCGGTGGCTGTGAATATGCAGGGCGTTGAACTACACACGAAACTCCACCTAGTACCCCCTACCCAATTCTCCGCG', 4, 12)
#substrings, positions = generate_all_substrings('abcdefg', 1, 7)
#print(substrings)
#print(positions)

