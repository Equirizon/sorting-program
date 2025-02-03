lst = [92, 88, 12, 77, 57, 100, 67, 38, 97, 89]
z = 1
#---------------------------------------------------------------------#
qlst = zlst = []
ctr = 1
test0 = lst.copy()
test1 = lst.copy()
test0.sort()
test1.sort(reverse=True)
if lst == test0 and z == 1 or lst == test1 and z == 2: 
    print('It is already sorted. \n' + str(lst))
else:
    while True:
        for call in range(0, len(lst)-1):
            qlst.append(lst[call])
            qlst.append(lst[call+1])
            lst.pop(call)
            lst.pop(call)
            if True:    
                print('Compared:' + str(qlst))
            #----------------#
            if z == 1:
                qlst.sort(reverse=True)
            elif z == 2:
                qlst.sort()
            #----------------#
            for i in qlst:
                lst.insert(call, i)
            qlst.clear()
            if True:
                print('Step '+ str(call) + ' ' + str(lst) + '\n')

        print('Pass '+ str(ctr) + ': ' + str(lst))
        print('------------------------------------')
        zlst = lst.copy()
        #----------------#
        if z == 1:
            zlst.sort()
        elif z == 2:
            zlst.sort(reverse=True)
        #----------------#
        if zlst == lst:
            print('Done!\nSorted list -> ' + str(lst) + '\n')
            break
        else:
            pass
        ctr += 1