print("Enter the number of frames: ", end= "")
capacity=4
f,fault,top,pf = [],0,0,'No'
print("Enter the reference string: ", end= "")
s=[7,0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
print("\nString|Frame →\t", end= '')
for i in range(capacity):
    print(i, end=' ')
print("Fault\n   ↓\n")
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
        else:
            f[top] = i
            top = (top+1)%capacity
        fault += 1
        pf = 'Yes'

    for x in f:
        print(x,end=' ')
    for x in range(capacity-len(f)):
        print(' ',end=' ')
    print(" %s"%pf)
print("\nTotal requests: %d\nTotal Page Faults: %d\n"%(len(s),fault))
