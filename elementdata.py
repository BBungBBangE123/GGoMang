import pandas as pd
import numpy as np

read = pd.read_csv('ab.csv')
data = read.dropna(how = 'any')
abr = np.array(data['Abriv.'])
ppt = np.array(data['Property'])
name = np.array(data.iloc[0:1, 3:])

sym = {}
for i in range(1, len(ppt)):
    sym[abr[i]]=[ppt[i], i]   #'Z': ['Atomic number', 1] 형태

num = {}
for i in range(0,118):
    num[name[0][i]]=i+1   #'H': 1 형태

def val(lst1=list(num.keys()), lst2=list(sym.keys())):   
    b =[0,2]
    d =[]
        
    for i in lst1:
            b.append(num[i]+2)
                   
    for i in lst2:
            d.append(sym[i][1])
          
    return data.iloc[d,b]

def rng(lst1,ppt):
    a = []
    b = {}
    
    for i in data.iloc[sym[ppt][1]]:
        a.append(i)
    
    for i in range(0,len(a[3:])):
        b[list(num.keys())[i]] =  a[3:][i]
        
    for i in list(num.keys()):
        if float(b[i]) >= float(lst1[0]) and float(b[i]) <= float(lst1[1]):
            pass
        
        else:
            del b[i]
    
    return b
    

   