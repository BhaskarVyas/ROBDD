#!/usr/bin/env python
# coding: utf-8

# In[1]:


import copy

def var_sep(cube):
    d = []
    for c in cube: 
        b = []
        a = list(c)
        a.append(" ") #for errpr rectifying, wouldn't detect last char otherwise
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

fn = input("Put function here: " )
cf_fn = input("put set of variable here: ")

cubes = fn.split('+')

fn_vars = var_sep(cubes)
cf_vars = var_sep(cf_fn.split(" "))#need to pass as list type, not string type
co_py = copy.deepcopy(fn_vars)



for i in range(len(cf_vars[0])):
    var = cf_vars[0][i]
    if co_py[0][0] == '1':
            break
   # print(co_py)
   # print(var)
   # p1 = 0
    a = 0
    b = [0]* len(co_py)
    for j in range(len(co_py)):
        #p2 = 0
        t = 0
        #print(str(j) + 'here')
        for h in range(len(co_py[j-a])):       
            #print(co_py[j-a][h-b[j-a]])
            if co_py and co_py[j-a] and var[0] == co_py[j-a][h-b[j-a]][0]:
               #print(var)
                if len(var) == len(co_py[j-a][h-b[j-a]]):
                    #co_py[p1].pop(p2)
                    #print(co_py[j-a][h])
                    co_py[j-a].pop(h-b[j-a])
                    b[j-a] = b[j-a]+1
                    #p2 = p2 - 1
                    #print("same")
                    if not co_py[j-a]:
                        co_py = [['1']]
                        #co_py = [['1']]
                        #print('1')
                        break
                else:
                    #co_py.pop(p1)   
                    #p1 = p1 - 1
                    #print(co_py[j-a])
                    co_py.pop(j-a)
                    t = 1
                    a = a + 1
                    #print('complement')
                    #p2 = p2 + 1
                    #print(p2)
                    #p1 = p1 + 1
                    #print(p1)
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
print(output)


# In[ ]:




