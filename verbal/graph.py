import json
import numpy as np
import os

FILE = '../static/data3000.json'
f = json.load(open(FILE))
all_words = set()
dic = {}
for lk in f:
    for uk in f[lk]:
        unit = f[lk][uk]
        for word in unit:
            for key in word:
                all_words.add(key)
                dic[key] = word[key]
                #for usage in word[key]:
                #    for syn in usage.get('synonym',[]):
                #        all_words.add(syn)

all_words = np.array(list(all_words))

def get_syn(word):
    s = set()
    for usage in dic.get(word,[]):
        s = s.union(usage.get('synonym',[]))
        #print(usage.get('synonym',[]))
    return s

def hasedge(a,b):
    a_syn = get_syn(a)
    b_syn = get_syn(b)
    return a in b_syn or b in a_syn

mat = np.zeros((len(all_words),len(all_words)))
mat.fill(1e10)

'''
words = []
for i in range(len(all_words)):
    print(i,end='\r')
    mat[i][i] = 0
    for j in range(i+1,len(all_words)):
        if all_words[i] in dic and all_words[j] in dic and hasedge(all_words[i],all_words[j]):
            mat[i][j] = mat[j][i] = 1
np.save('g.npy',mat)
'''
#mat = np.load('g.npy')

'''
for k in range(len(all_words)):
    mat_new = np.zeros((len(all_words),len(all_words)))
    for i in range(len(all_words)):
        for j in range(len(all_words)):
            print((i,j,k),end='\r')
            mat_new[i,j] = min(mat[i,j],mat[i,k]+mat[k,j])
    mat = mat_new
np.save('mat.npy',mat)
'''

u = np.arange(0,len(all_words))

def merge(u,i,j):
    u[j] = i

for i in range(len(all_words)):
    for j in range(i+1,len(all_words)):
        wa = all_words[i]
        wb = all_words[j]
        #print(wa,wb)
        if hasedge(wa,wb):
            print(wa,wb)
            merge(u,i,j)

print(u)
np.save('u.npy',u)

u = np.load('u.npy')
ss = []
f = -np.ones(len(all_words),dtype=int)

max_h = 0
for i in range(len(all_words)):
    s = []
    set_idx = -1
    cnt = 0
    while u[i] != i:   
        print(all_words[u[i]],all_words[i])         
        if f[i] != -1:
            set_idx = f[i]
            break       
        s.append(i) 
        i = u[i]
        cnt += 1
    max_h = max(cnt,max_h)
    if set_idx == -1:
        s.append(i)
        set_idx = len(ss)
        ss.append(s)
    else:
        ss[set_idx].extend(s)
    for item in s:
        f[item] = set_idx

print(max_h)
for i in range(len(ss)):
    s = ss[i]
    for j in range(len(s)):
        s[j] = all_words[s[j]]

with open('../static/syn.json','w') as f:
    json.dump(ss,f,indent=4)
    