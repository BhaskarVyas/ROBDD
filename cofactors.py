# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:23:54 2020

@author: Bhaskar Vyas
"""
from itertools import islice

def var_sep(cube):
    d = []
    for c in cube: 
        b = []
        a = list(c)
        a.append(" ") #for err rectifying, woudln't detect last char otherwise
        for i in range(len(a)-1):
            if a[i+1] == "'":
                l = "".join(a[i]+a[i+1])
            elif a[i] == "'" or a[i] == " ":
                continue
            else:
                l = a[i]
            b.append(l)
        d.append(b)
    return d

fn = input("Put function here: " )
cf_fn = input("put set of variable here: ")

cubes = fn.split('+')

fn_vars = var_sep(cubes)
cf_vars = var_sep(cf_fn.split(" "))#need to pass as list type, not string type

for i in range(len(cf_vars[0])):
    var = cf_vars[0][i]
    p1 = 0
    for j in fn_vars:
        p2 = 0
        for h in j:
            if var[0] == h[0]:
                if len(var) == len(h):
                    fn_vars[p1].pop(p2)
                else:
                    fn_vars.pop(p1)                 
            p2 = p2 + 1
        p1 = p1 + 1

i = []
for j in fn_vars:
    i.append("".join(j))
output = "+".join(i)
print(output)