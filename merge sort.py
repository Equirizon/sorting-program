lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
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
    ln = len(lst)
    n = 1   
    while ln//2 != 1 and ln//2 != 2 :
        ln = ln//2                  #Determines how many divisions/level in the
        n += 1                      #given list before reaching its atomic value
    if False:
        print('Number of Sub-levels: ' + str(n))
    if len(lst) > 2**(n+1):
        S = 2
        s = 1                       #Adds an extra array if the len(lst) is
    else:                           #not a perfect square 
        S = 0
        s = 0
    for i in range(1,n+2+s):        #Responsible for number of sublevels/levels generated
        qlst.clear()
        x = 0
        y = x + (2**i)              #Number of elements per each sub-level 'n'
        q = (2**(n+1))//(2**i)+S    #Number of arrays per each sub-level 'n'
        for a in range(q):          #Responsible for number of arrays generated
            if False:
                print('------------------')
                if len(lst[x:y]) != 0:
                    print('Sub-level:'+str(i)+' Array#'+ str(a+1)+': '+str(lst[x:y]))
                    
            zlst = lst[x:y]
            #----------------#
            if z == 1:
                zlst.sort()
            elif z == 2:
                zlst.sort(reverse=True)
            #----------------#
            if len(lst[x:y]) != 0:
                qlst.append(zlst)
            x += 2 ** i             #Increment from main list 'lst'
            y += 2 ** i
        print('\nLevel ' + str(i) +' '+ str(qlst))
        print('------------------------------------\n')
        if False:
            en = input('press any key >_')
    print('\nDone!\nSorted list -> Pass#' + str(i) +' '+ str(qlst) + '\n')
    print('<!--Listception-->')