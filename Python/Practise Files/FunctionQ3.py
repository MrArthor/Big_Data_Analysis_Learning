"""
Created on Thu Oct 17 12:01:35 2024

@author: mr-arthor
"""

def Factorial(inte):
    for i in range (1,inte):
        fact=1
        for j in range(1, i+1):
            fact*=j
        print(fact)


Factorial(10)
