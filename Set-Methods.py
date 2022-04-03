# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:52:56 2022

@author: Santhanagopalan
"""

E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}
print('E:', E, '\nN:', N)
print('Union of E and N is', E.union(N))
print('Intersection of E and N is', E.intersection(N))
print('Difference of E and N is', E.difference(N))
print('Symmetric Difference of E and N is', E.symmetric_difference(N))
