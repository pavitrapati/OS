def closest(lst, K):      
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

d=list(map(int,input().split()))
h=int(input())
t=0
for i in range(len(d)):
    t+=abs(closest(d,h)-h)
    h=closest(d,h)
    d.remove(h)
print(t)