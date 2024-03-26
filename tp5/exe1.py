from collections import defaultdict

s = [('y', 1), ('b',2), ('y', 3), ('b', 4), ('r', 1)]
d=defaultdict(list)
for k, v in s: 
    d[k].append(v)
print(d.items())

s='mississippi'
d=defaultdict(int)
for k in s:
    d[k]+=1
print(d.items())