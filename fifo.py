d=list(map(int,input().split()))
h=int(input())
t=0
for i in d:
    t+=abs(i-h)
    h=i
print(t)