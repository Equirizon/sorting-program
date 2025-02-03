lst = [14,33,27,10,35,19,42,44]
z = 1
#---------------------------------------------------------------------#
qlst = zlst = []
test0 = lst.copy()
test1 = lst.copy()
test0.sort()
test1.sort(reverse=True)
if lst == test0 and z == 1 or lst == test1 and z == 2: 
    print('It is already sorted. \n' + str(lst))
else:
    while True:
        for call in range(1, len(lst)):
            if call == 1:
                qlst.append(lst[0])
                qlst.append(lst[1])
                #----------------#
                if z == 1:
                    qlst.sort()
                elif z == 2:
                    qlst.sort(reverse=True)
                #----------------#
                lst.pop(0)
                lst.pop(0)
                if False:
                    print('Index 0,1 appended: ' + str(qlst))
            else:
                qlst.append(lst[0])
                #----------------#
                if z == 1:
                    qlst.sort()
                elif z == 2:
                    qlst.sort(reverse=True)
                #----------------#
                lst.pop(0)
            if False:
                if len(lst) == 0:
                    print('Insert: [Empty]')
                else:
                    print('Insert: ' + str(lst))
                print('Inserted: ' + str(qlst))
            zlst = qlst + lst
            print('Pass ' + str(call) + ': ' + str(zlst))
            print('------------------------------------')
            if len(lst) == 0:
                print('Done!\nSorted list -> ' + str(zlst) + '\n')
                break
        break