#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:34:06 2021

@author: Matthew
"""

data = input('What is your input data?')

def split(word):
    return[char for char in word]

def join(word):
    while len(word) > 1:
        word[0] = word[0] + word[1]
        word.pop(1)
    return word

bases = ['A', 'C', 'G', 'T']

def parse(data):
    letters = split(data)
    breakers = []
    for i in range(len(letters)-1):
        if letters[i] == '\n' and letters[i-1] not in bases or letters[i] == '\n' and letters[i+1] not in bases: 
            breakers.append(i)
    string = letters[(breakers[0]+1):-1] + [letters[-1]]
    return(string)

def reverse(letters):
    num_bases = len(letters)
    reversed_letters = []
    for i in range(num_bases):
        position = num_bases - 1 - i
        reversed_letters.append(letters[position])
    return(reversed_letters)

def complementary(letters):
    num_bases = len(letters)
    complementary_letters = []
    for i in range(num_bases):
        if letters[i] == 'A':
            complementary_letters.append('T')
        elif letters[i] == 'T':
            complementary_letters.append('A')
        elif letters[i] == 'G':
            complementary_letters.append('C')
        elif letters[i] == 'C':
            complementary_letters.append('G')
    return complementary_letters

def reverse_complementary(data):
    reversed_letters = reverse(data)
    reversed_complementary_letters = complementary(reversed_letters)
    return(reversed_complementary_letters)

def find_substrings(data):
    string = parse(data)
    substrings = []
    positions = []
    for i in range(len(string)):
        remaining_letters = len(string) - i
        if remaining_letters > 11:
            for j in range(4, 13): #length of substrings from 4 to 12
                substrings.append(string[i:(i+j)])
                positions.append(i)
        elif remaining_letters <= 11 and remaining_letters > 3:
            for j in range(4, remaining_letters + 1):
                substrings.append(string[i:(i+j)])
                positions.append(i)
                
    reverse_palindrome_sites = []
    reverse_palindrome_lengths = []
    a = substrings[0]
    for i in range(len(substrings)):
        if reverse_complementary(substrings[i]) == substrings[i]:
            reverse_palindrome_sites.append(positions[i] + 1)
            reverse_palindrome_lengths.append(len(substrings[i]))
    for i in range(len(reverse_palindrome_sites)):
        print(f'{reverse_palindrome_sites[i]}' + ' ' + f'{reverse_palindrome_lengths[i]}')
            

find_substrings(data)

                
        
            
        
    