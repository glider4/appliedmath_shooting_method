#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:16:52 2018

@author: mathemacode
Shooting Method

"""
import numpy as np

def shooting():
    # alpha and beta are the same
    alpha = np.log(8*(np.pi**2))
    beta = np.log(8*(np.pi**2))
    
    # define exact equation to test 
    def equation(t):
        c1 = (8*(np.pi**2))
        c2 = 0
        sol = np.log(c1) - 2*np.log(np.cos(0.9939931166*t) + c2)
        return sol
    
    i = 0
    solution = [ ]
    valset = [ ]
    
    # formula to solve for Z3 - using a, A, b, B for ease
    def newZ(a, A, b, B):
        VAL = a + (beta - A)*( (a - b) / (A - B) )
        return VAL
    
    # initial Z1 and Z2 given
    Z = (-23/2)
    Zm1 = (-25/2)
    
    valset.append(Zm1)
    valset.append(Z)
    
    while i < 11:
        VAL = newZ(Z, equation(Z), Zm1, equation(Zm1))
        
        # redefine values for next iteration
        Zm1 = Z
        Z = VAL
        
        # move onto next iteration
        i += 1
        
        valset.append(VAL)
        
        # append equation result of new Z into solution set
        solution.append(equation(Z))
        
    print("\nMathemacode: Shooting Method Results")
    print("====================================================\n")
    print("     Solution Convergence Demonstration:\n ")
    print("   Z Value                 Solution")
    
    for i in range(0,2):
        print(" ", valset[i], " \t\t", solution[i])
        
    for i in range(2,11):
        print(" ", valset[i], " \t", solution[i])
        
        
    print("\nCompare to actual solution:", alpha)
    print("====================================================\n")
    
shooting() 