lst = [14,33,27,10,35,19,42,44]
z = 1
#---------------------------------------------------------------------#
qlst = zlst = []
call = 0
test0 = lst.copy()
test1 = lst.copy()
test0.sort()
test1.sort(reverse=True)
if lst == test0 and z == 1 or lst == test1 and z == 2: 
    print('It is already sorted. \n' + str(lst))
else:
    for i in range(0,len(lst)):
        ctr = 0
        #----------------#
        if z == 1:
            mn = min(lst)
        elif z ==2:
            mn = max(lst)
        #----------------#
        for i in lst:
            ctr += 1
            if i == mn:
                pos = ctr - 1 + call
        call += 1
        lst.remove(mn)
        qlst.append(mn)
    #-------------------------#
        zlst = qlst + lst
        zlst.pop(call)
        zlst.insert(pos,lst[0])
        if False:
            print('Call: ' + str(call))
            print('Position: ' + str(pos))
            print('Left: ' + str(lst))
            print('Sorted: ' + str(qlst) + '\n')
        print('Pass '+ str(call) +': ' + str(zlst))
        srtd = zlst.copy()
        #----------------#
        if z == 1:
            srtd.sort()
        elif z == 2:
            srtd.sort(reverse=True)
        #----------------#
        if zlst == srtd:
            print('Done!\nSorted list -> ' + str(zlst) + '\n')
            break
        for i in qlst:
            zlst.remove(i)
        lst = zlst
        if False:
            print('\nSorted removed: ' + str(zlst))
        print('------------------------------------')