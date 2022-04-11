s=list(map(int,input().split()))
p=list(map(int,input().split()))
f=[0]*len(s)
for i in range(len(p)):
    tmp=s[:]    
    print(tmp,s)
    while len(tmp)>0:
        if p[i]<=min(tmp) and f[tmp.index(min(tmp))]==0:
            f[tmp.index(min(tmp))]=p[i]
            break
        else:    
            tmp.remove(min(tmp))

print(f)