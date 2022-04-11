print("LRU Page Replacement Algorithm\n")
processlist=[7,0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4
s = []
pageFaults = 0
for i in processlist:
    if i not in s:
        if len(s) == capacity:
            s.remove(s[0])
            s.append(i)
        else:
            s.append(i)
        pageFaults += 1
    else:
        s.remove(i)
        s.append(i)

print("The number of page faults: ", pageFaults, "\n")