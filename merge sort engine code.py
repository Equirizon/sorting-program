lst = [14,33,27,10,35,19,42,44,18,72,63,54,45,36,27,18]
qlst = zlst = []
ln = len(lst)
n = 1
while ln//2 != 2:
    ln = ln//2
    n += 1    #Number of divisions/levels before atomic value
print('Main list: ' + str(lst) +'\nNumber of levels: ' + str(n))
for i in range(1, n+2):
    qlst.clear()
    x = 0
    y = x + (2**i)  #Number of elements per each level 'n' (n^2)
    q = len(lst)//(2**i) #Number of arrays per each level 'n' (length of list/n^2)
    for a in range(q):
        print(lst[x:y])
        zlst = lst[x:y]
        zlst.sort()
        qlst.append(zlst)
        print(qlst)
        x += 2 ** i  #Increment from main list 'lst'
        y += 2 ** i