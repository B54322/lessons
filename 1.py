
col = int(input())
d = []

for i in range(col):
    d.append(int(input()))
    
not_even = [i for i in d if i % 2 != 0]
even = [i for i in d if i % 2 == 0]

m_e = 0
m_n_e = 0
if len(not_even) != 0: 
    m_n_e = min(not_even)
if len(even) != 0: 
    m_e = min(even)   

m =  m_e + m_n_e

def do(m, d):
    if d<m:
        return d + m
    else:
        return d

dd = []        
for i in d:
    dd.append(do(m, i))

print(*dd)
