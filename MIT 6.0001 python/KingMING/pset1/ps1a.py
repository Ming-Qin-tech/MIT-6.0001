# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = 0.0
'''
y is the down price of the house
'''
y = float(input("please input the price of your dream house"))
y = y * 0.25
'''
z is the deposit money of every month
''' 
z = float(input("please input your annual salary"))
z = z*0.1 / 12
m = 0
while x < y:
    x = x * 0.04 /12 + z + x
    m = m + 1
# m is the number of month
print(m)    