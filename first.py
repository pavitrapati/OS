# storage process flag
s=list(map(int,input().split()))
p=list(map(int,input().split()))
f=[0]*len(s)
for i in range(len(p)):
    for j in range(len(s)):
        if p[i]<=s[j] and f[j]==0:
            f[j]=p[i]
            break
for a in range(len(f)):
    if f[a]!=0:
        print(f[a],a+1)