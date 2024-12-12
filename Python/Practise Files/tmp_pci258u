#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:10:44 2024

@author: mr-arthor
"""

# =============================================================================
# Write a function translate() that will translate a text into "rövarspråket" (Swedish for
# "robber's language"). That is, double every consonant and place an occurrence of "o" in
# between. For example, translate("this is fun") should return the string "tothohisos isos
# fofunon".
# =============================================================================


def Translate(txt):
    temp=[]
    for x in txt:
        if x not in 'aioue ':
           temp.append(x)
           temp.append('O')
        temp.append(x)
    temp= "".join(temp)
    return temp

print(Translate("this is fun"))


print ("hello world",end=" ")
print("How are you")
