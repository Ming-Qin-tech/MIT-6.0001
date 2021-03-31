# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:02:59 2021

@author: qinming
"""
import numpy as np
x = 0.0
'''
y is the down price of the house
'''
y = float(input("please input the price of your dream house: "))
y = y * 0.25
'''
z is the deposit money of every month
''' 
zb = float(input("please input your annual salary: "))
# r = float(input("please input how much percent of salary you want to deposit for house: "))
z = zb
r = 1

k = float(input("please enter the semi-annual  raise: "))
z = z*r / 12
m = 0
sum = 0
    
while m < 36:
    x = x * 0.04 /12 + z + x
    m = m + 1
    if m % 6 == 0:
        z = z * (1 + k)
if x < y and x + 100 < y:
    print("It is not possible to pay the down payment in three years.")
elif np.abs(y-x) < 100:
    print("Best savings rate:​ 1.0000")
else:
    rmax = 10000
    rmin = 0
    n=1
    while 1:
        n = n + 1
        r = (rmax + rmin) / 2
        m = 0
        x = 0.0
        z = zb
        z = z * r / 10000 /12
        while m < 36:
            x = x * 0.04 /12 + z + x
            m = m + 1
            if m % 6 == 0:
                z = z * (1 + k)
        if np.abs(y-x) < 100:
            print("Best savings rate:​ ", format(r/10000,'.4f'))
            print("Steps in bisection search: ", n)
            break
        elif x < y:
            rmin = r
        else:
            rmax = r
            
    
        
   