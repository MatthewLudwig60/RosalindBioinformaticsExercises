#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:34:42 2021

@author: Matthew
"""
infants = [1]
adults = [0]
rabbits = [1]
births = [0]
deaths = [0]
maturations = [0]
def mortal_rabbits(n, m):
    for i in range(1, n): #2nd to 6th month
        maturations.append(infants[i-1])
        if i >= 2:
            births.append(adults[i-1])
        else:
            births.append(0)
        if i >= m:
            deaths.append(maturations[i-(m-1)])
        else:
            deaths.append(0)
        infants.append(infants[i-1] + births[i] - maturations[i])
        adults.append(adults[i-1] + maturations[i] - deaths[i])
        rabbits.append(infants[i] + adults[i])
    print(rabbits[-1])
mortal_rabbits(80, 20)

    
        
    