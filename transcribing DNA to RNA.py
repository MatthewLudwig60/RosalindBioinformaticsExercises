#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:19:45 2021

@author: Matthew
"""

def split(word):
    return[char for char in word]
def join(word):
    while len(word) > 1:
        word[0] = word[0] + word[1]
        word.pop(1)
    return word
data = input('What is your DNA nucleotide sequence?')
def transcribe(data):
    letters = split(data)
    for i in range(len(letters)):
        if letters[i] == 'T':
            letters[i] = 'U'
    word = join(letters)
    print(word)
transcribe(data)