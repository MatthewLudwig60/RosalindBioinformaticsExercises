#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:06:12 2021

@author: Matthew
"""
import numpy as np

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
    Parsed_lines = []
    for i in range(1, len(lines)+1, 2):
        dummy = split(lines[i][0])
        place = []
        for i in range(len(dummy)):
            if dummy[i] != '\n':
                place.append(dummy[i])
        Parsed_lines.append(place)
    return(Parsed_lines)

def DNA_matrix(data):
    Parsed_lines = parse(data)
    matrix = np.zeros((4, len(Parsed_lines[0])))
    for i in range(len(Parsed_lines)):
        for j in range(len(Parsed_lines[0])):
            for k in range(len(bases)):
                if Parsed_lines[i][j] == bases[k]:
                    matrix[k][j] += 1
    return(matrix)

def consensus_string(data):
    matrix = DNA_matrix(data)
    string = ''
    for i in range(len(matrix[0])):
        position = 0
        dummy = 0
        for j in range(4):
            if matrix[j][i] > dummy:
                dummy= matrix[j][i]
                position = j
        string += bases[position]
    print(string)
    A_line = 'A: '
    C_line = 'C: '
    G_line = 'G: '
    T_line = 'T: '
    for i in range(len(matrix[0])):
        A_line += f'{str(int(matrix[0][i]))} '
        C_line += f'{str(int(matrix[1][i]))} '
        G_line += f'{str(int(matrix[2][i]))} '
        T_line += f'{str(int(matrix[3][i]))} '
        
    print(A_line)
    print(C_line)
    print(G_line)
    print(T_line)
        
    
consensus_string(data)








