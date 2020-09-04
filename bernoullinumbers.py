# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:49:12 2020

@author: spiku
"""

# https://wstein.org/projects/168/kevin_mcgown/bernproj.pdf

from decimal import *
import math
import functools as fn
import numpy as np

pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286')

def factorial(n): 
    lis = [x for x in range(1, n+1)]
    return fn.reduce(lambda a,b:a*b,[1] + lis)

def prime_sieve(n):
    """it generates res, list of all primes < n, and prime_list, all non-primes < n, excluding 1"""
    prime_list = []
    res = []
    for i in range(2, n+1):
        if i not in prime_list:
            res.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
    return res

# McGown algorithm
def b(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0.5
    elif (n-1)%2 == 0:
        return 0
    else:
        K = 2*factorial(n)*(1/Decimal((2*pi)**n))
        primes = prime_sieve(n+1)
        d = Decimal(1)
        f = lambda x, y: Decimal(x*y)
        lis1 = [p for p in primes if n%(p-1) == 0]
        for i in lis1:
            d *= i
        N = math.ceil((K*d)**(Decimal(1.0/(n-1))))
        z = Decimal(1)
        lis2 = [p for p in primes if p <= N]
        for i in lis2:
            z *= 1/(1-1/(Decimal(i)**n))
        a = Decimal(((-1)**(n/2+1)) * math.ceil(Decimal(d*K*z)))
        if a == Decimal(0):
            a = (-1)**(n/2+1)
        print(a,'\n',d)
        return a/d
    
n = int(input("Enter the index of the Bernoulli number: "))

if n > 28:
    getcontext().prec = n

print(b(n))