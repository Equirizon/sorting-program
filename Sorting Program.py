
import os
clear = lambda: os.system('cls')
clear()
equirizon = 1
eqn = 'False'
Q = 'Disabled'
#x elements
#y type
#z sort
#q append

def main_menu(y):
    if y == 1: #int
        print('Enter your ' + str(x) + ' integer/s: ')
        while True:
            try:
                for i in range(1,x+1):
                    q = int(input('Please enter element#' + str(i) + ' '))
                    lst.append(q)
            except:
                ckr = input('That seems to be a letter, it should be a number/integer. Please try again...')
                lst.clear()
                continue
            break

    elif y == 2: #str
        print('Enter your ' + str(x) + ' letter/s: ')
        ckr = 'True'
        while ckr == 'True':
            for i in range(1,x+1):
                try:
                    q = input('Please enter element#' + str(i) + ' ')
                    ckr = int(q)
                    ckr = input('I\'m afraid that\'s not a letter, User. Please try again...')
                    ckr = 'True'
                    lst.clear()
                    break
                except:
                    lst.append(q)
                    ckr = 'False'

    print('\n\nHere\'s your list ' + str(lst) + '\n')

def selection_sort(lst,z):
    qlst = []
    zlst = []
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
            elif z == 2:
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
            if eqn == 'True':
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
            if eqn == 'True':
                print('Sorted removed: ' + str(zlst))
            print('------------------------------------')

def bubble_sort(lst,z):
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
                if eqn == 'True':    
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
                if eqn == 'True':
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

def insertion_sort(lst,z):
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
                    if eqn == 'True':
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
                if eqn == 'True':
                    if len(lst) == 0:
                        print('Insert: [Empty]')
                    else:
                        print('Insert: ' + str(lst))
                    print('Inserted: ' + str(qlst) + '\n')
                zlst = qlst + lst
                print('Pass ' + str(call) + ': ' + str(zlst))
                print('------------------------------------')
                if len(lst) == 0:
                    print('Done!\nSorted list -> ' + str(zlst) + '\n')
                    break
            break

def merge_sort(lst,z):
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
        if eqn == 'True':
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
                if eqn == 'True':
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
            if eqn == 'True':
                input('press any key >_')
        print('\nDone!\nSorted list -> Pass#' + str(i) +' '+ str(qlst) + '\n\n<!--Listception-->')
#---------------------------------------------------------------------#
chk = 'True'
while chk == 'True':
    lst = []
    try:
        print('''
    *************** SORTING ALGORITHM APPLICATION ****************
    |                  Programmed By: Brandon                    |
    |                       BSCPE 2 - 4                          |
    |                                                            |
    |                    <<< MAIN MENU >>>                       |
    |                                                            |
    |                 [1] Selection Sorting                      |
    |                 [2] Bubble Sorting                         |
    |                 [3] Insertion Sorting                      |
    |                 [4] Merge Sorting                          |
    |                                                            |
    |                [0] Toggle Advanced Mode                    |
    |                                                            |''')
        print('    |Advanced mode: '+ Q +'                                     |')
        x = int(input('''    **************************************************************

    Select an option: '''))
    except:
        ckr = input('Wrong input, press any key to continue...')
        clear()
        continue

    if x == 1:
        while True:
            try:
                x = int(input('How many elements in your list? '))
                y = int(input('\nEnter type of element.\n\n[1] Integer\n[2] Letters\n-> '))
                z = int(input('Sort by?\n\n[1] Ascending/A-Z\n[2] Descending/Z-A\n-> '))

                if x >= 2: #Filter
                    pass
                else:
                    ckr = input('Minimun elements in list should be two (2), please try again. Press any key to continue...')
                    continue
                
                if z == 1: #Filter/Indicator
                    a = 'Ascending'
                elif z == 2:
                    a = 'Descending'
                else:
                    ckr = input('Choice out of range, please try again. Press any key to continue...')
                    continue

                if y == 1: #Filter
                    pass
                elif y == 2:
                    pass
                else:
                    ckr = input('Choice out of range, please try again. Press any key to continue...')
                    continue

                main_menu(y)
                print('Sorting algorithm used: Selection Sort\nSort by: ' + str(a) + '\n')
                if eqn == 'True':
                    print('[Advanced Mode Enabled]')
                selection_sort(lst,z)
                break
            except:
                ckr = input('Wrong input, press any key to continue...')
                continue

    elif x == 2:
        while True:
            try:
                x = int(input('How many elements in your list? '))
                y = int(input('\nEnter type of element.\n\n[1] Integer\n[2] Letters\n-> '))
                z = int(input('Sort by?\n\n[1] Ascending/A-Z\n[2] Descending/Z-A\n-> '))
                
                if x >= 2: #Filter
                    pass
                else:
                    ckr = input('Minimun elements in list should be two (2), please try again. Press any key to continue...')
                    continue
                
                if z == 1: #Filter/Indicator
                    a = 'Ascending'
                elif z == 2:
                    a = 'Descending'
                else:
                    ckr = input('Choice out of range, please try again. Press any key to continue...')
                    continue

                if y == 1: #Filter
                    pass
                elif y == 2:
                    pass
                else:
                    ckr = input('Choice out of range, please try again. Press any key to continue...')
                    continue

                main_menu(y)
                print('Sorting algorithm used: Bubble Sort\nSort by: ' + str(a) + '\n')
                if eqn == 'True':
                    print('[Advanced Mode Enabled]')
                bubble_sort(lst,z)
                break
            except:
                ckr = input('Wrong input, press any key to continue...')
                continue
    
    elif x == 3:
        while True:
            try:
                x = int(input('How many elements in your list? '))
                y = int(input('\nEnter type of element.\n\n[1] Integer\n[2] Letters\n-> '))
                z = int(input('Sort by?\n\n[1] Ascending/A-Z\n[2] Descending/Z-A\n-> '))
                
                if x >= 2: #Filter
                    pass
                else:
                    ckr = input('Minimun elements in list should be two (2), please try again. Press any key to continue...')
                    continue
                
                if z == 1: #Filter/Indicator
                    a = 'Ascending'
                elif z == 2:
                    a = 'Descending'
                else:
                    ckr = input('Choice out of range, please try again. Press any key to continue...')
                    continue

                if y == 1: #Filter
                    pass
                elif y == 2:
                    pass
                else:
                    ckr = input('Choice out of range, please try again. Press any key to continue...')
                    continue

                main_menu(y)
                print('Sorting algorithm used: Insertion Sort\nSort by: ' + str(a) + '\n')
                if eqn == 'True':
                    print('[Advanced Mode Enabled]')
                insertion_sort(lst,z)
                break
            except:
                ckr = input('Wrong input, press any key to continue...')
                continue
            
    
    elif x == 4:
        while True:
            try:
                x = int(input('How many elements in your list? '))
                y = int(input('\nEnter type of element.\n\n[1] Integer\n[2] Letters\n-> '))
                z = int(input('Sort by?\n\n[1] Ascending/A-Z\n[2] Descending/Z-A\n-> '))
                
                if x >= 2: #Filter
                    pass
                else:
                    ckr = input('Minimun elements in list should be two (2), please try again. Press any key to continue...')
                    continue
                
                if z == 1: #Filter/Indicator
                    a = 'Ascending'
                elif z == 2:
                    a = 'Descending'
                else:
                    ckr = input('Choice out of range, please try again. Press any key to continue...')
                    continue

                if y == 1: #Filter
                    pass
                elif y == 2:
                    pass
                else:
                    ckr = input('Choice out of range, please try again. Press any key to continue...')
                    continue

                main_menu(y)
                print('Sorting algorithm used: Merge Sort\nSort by: ' + str(a) + '\n')
                if eqn == 'True':
                    print('[Advanced Mode Enabled]')
                merge_sort(lst,z)
                break
            except:
                ckr = input('Wrong input, press any key to continue...')
                continue

    elif x == 0:
        equirizon +=1
        if equirizon % 2 == 0:
            eqn = 'True'
            Q = 'Enabled '
        else:
            eqn = 'False'
            Q = 'Disabled'
        chk = 'True'
        clear()
        continue

    else:
        ckr = input('Choice out of range, please try again. Press any key to continue...')
        clear()
        continue
    
    while True:
        chkr = str(input('Do you want to try again? Y/N '))
        if chkr == 'n' or chkr == 'N':
            chk = 'False'
            break
        elif chkr == 'y' or chkr == 'Y':
            chk = 'True'
            clear()
            break
        else:
            print("Wrong input please try again...")
            continue
clear()
print('''
    SORTING ALGORITHM APPLICATION


    @Equirizon 2020 | @Equirzn''')


# @Equirizon 2020 | @Equirzn