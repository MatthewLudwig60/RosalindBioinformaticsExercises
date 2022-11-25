#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:17:08 2021

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

def parse(data):
    letters = split(data)
    breakers = []
    for i in range(len(letters)-1):
        if letters[i] == ' ':
            breakers.append(i)
    lines = []
    for i in range(len(breakers)+1):
        if i == 0:
            line = join(letters[0:breakers[0]])
        elif i == len(breakers):
            line = join(letters[(breakers[i-1]+1):(-1)])
            line.append(letters[-1])
            line = join(line)
        else:
            line = join(letters[(breakers[i-1]+1):breakers[i]])
        lines.append(line)
    return(lines)

def expected_formula(a, b, c, d, e, f):
    return(2*a + 2*b + 2*c + 1.5*d + e)

def expected_offspring(data):
    values = parse(data)
    a = int(values[0][0])
    b = int(values[1][0])
    c = int(values[2][0])
    d = int(values[3][0])
    e = int(values[4][0])
    f = int(values[5][0])
    output = expected_formula(a, b, c, d, e, f)
    print(output)

expected_offspring(data)
    