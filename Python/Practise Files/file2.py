#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:27:21 2024

@author: mr-arthor
"""
list_fun =["Fun","Not So Fun","cloud"]


print(list_fun)

print (list_fun[2])


if "Funny" in list_fun:
    print("yes")
else:
    print("no")
    
    
list_fun.append("Artificial Intelligence ");

list_fun.insert(10,"wht");


print(list_fun)
list_fun.remove("Fun")
print(list_fun)

list_fun.sort(reverse=True)
print(list_fun)
list_fun.clear()
print(list_fun)


