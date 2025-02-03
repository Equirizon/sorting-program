lst = [14,33,27,10,35,19,42,44]
qlst = []
call = -1
for i in range(0,len(lst)):
    call += 1
    ctr = 0
    mn = min(lst)
    for i in lst:
        ctr += 1
        if i == mn:
            pos = ctr - 1
    lst.pop(pos)
    qlst.append(mn)
    print(pos)
    print(lst)
    print(qlst)
    print('-----------------------------------------')

    
    

