lst = []
while True:
    y = int(input('int/str-> '))
    x = int(input('count-> ')) 
    if y == 1: #int
        print('Enter your ' + str(x) + ' integer/s: ')
        while True:
            try:
                for i in range(1,x+1):
                    q = int(input('Please enter element#' + str(i) + ' '))
                    lst.append(q)
            except:
                ckr = input('It should be an integer please try again...')
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
                    break
                except:
                    lst.append(q)
                    ckr = 'False'
    else:
        print('Incorrect input, please try again...')
        continue
    print('\n\nHere\'s your list ' + str(lst) + '\n')
    break