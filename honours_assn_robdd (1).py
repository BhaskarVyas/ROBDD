#!/usr/bin/env python
# coding: utf-8

# In[11]:


import copy

class node:
    def __init__(self, val = None):
        self.var = val
        self.high = None
        self.low = None
        self.printed = 0
        
node_low = node("0")
node_high = node("1")

def get_put_UT(key, node_):
    if key in unique_table.keys():
        #print(1)
        return unique_table[key]
    else:
        unique_table[key] = node_
        return node_

def var_sep(cube):
    d = []
    for c in cube: 
        b = []
        a = list(c)
        a.append(" ") #for error rectifying, wouldn't detect last char otherwise
        for i in range(len(a)-1):
            if a[i+1] == "'":
                l = "".join(a[i]+a[i+1])
            elif a[i] == "'" or a[i] == " ":
                continue
            else:
                l = a[i]
            b.append(l)
            for z in range(len(b)):
                for y in range(len(b)):
                    x = y+z+1
                    if x<len(b) and b[z] == b[x]:
                        b.pop(x)
                        x = x-1
        d.append(b)
    return d

def cofactor(fn,var_):
    cubes = fn.split('+')
    fn_vars = var_sep(cubes)
    cf_vars = var_sep(var_.split(" "))#need to pass as list type, not string type
    co_py = copy.deepcopy(fn_vars)
    #print(cf_vars)
    for i in range(len(cf_vars[0])):
        var = cf_vars[0][i]
        #print("cof debug 1 " +var)
        #print(co_py)
        if co_py[0][0] == '1':
            break
        a = 0
        b = [0]* len(co_py)
        for j in range(len(co_py)):
            #print(co_py)
            #print(j-a)
            t = 0
            #print(co_py[j-a])
            for h in range(len(co_py[j-a])):       
                if co_py and co_py[j-a] and var[0] == co_py[j-a][h-b[j-a]][0]:
                    if len(var) == len(co_py[j-a][h-b[j-a]]):
                        co_py[j-a].pop(h-b[j-a])
                        b[j-a] = b[j-a]+1
                        
                        if not co_py[j-a]:
                            co_py = [['1']]
                            break
                    else:
                        co_py.pop(j-a)
                        t = 1
                        a = a + 1

                    if t == 1:
                        break
            if not co_py:
                co_py = [['0']]
            elif co_py[0][0] == '1':
                break 
    i = []
    for j in co_py:
        i.append("".join(j))
    output = "+".join(i)
    return output

def depth_first_traversals_inorder(top): 
    if top: 
        depth_first_traversals_inorder(top.low) 
        print(top.var)
        depth_first_traversals_inorder(top.high) 

        #if root.printed == 0:
        #print(root.var, end= " ")
        #root.printed = 1

def ite(function, variable_order, i):
    var = variable_order[i]
    #print("var :" + var)
    #print("function :"+ function)
    cofactor_high = cofactor(function, var)
    #print(cofactor_high)
    var_bar = var+"'"
    #print("var_bar :"+var_bar)
    cofactor_low = cofactor(function, var_bar)
    #print(cofactor_low)
    
    key = var + cofactor_high + cofactor_low
    #print(key)
    
    node_ = node(var)
    if cofactor_high=="0":
        node_.high = node_low
    if cofactor_high=="1":
        node_.high = node_high
    if cofactor_low=="0":
        node_.low = node_low
    if cofactor_low == "1":
        node_.low = node_high
        
    if node_.high == None:
        node_.high = ite(cofactor_high, variable_order, i+1)
    if node_.low == None:
        node_.low = ite(cofactor_low, variable_order, i+1)
    
    node_ = get_put_UT(key, node_)
    if node_.high == node_.low:
        return node_.high
    return node_

unique_table = {}

fn = input('Enter function here: ')
var_order = list(input('Enter variable order here: '))

robdd = ite(fn, var_order, 0)

print("depth_first_traversals_inorder")
depth_first_traversals_inorder(robdd)


# In[ ]:





# In[ ]:




