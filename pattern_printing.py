n = 'y'
while n == 'y':
    try:
        num = int(input("Enter the number:- "))
        pattern = int(input("Enter the pattern style (i.e. 1(simple) or 0(reverse)):- "))
    except:
        print('Wrong Input! You can only chose numbers as your input')
    else:
        if pattern == 0 or pattern == 1:
            pattern = bool(pattern)
            if pattern is True:
                num1 = 1
                while num1 in range(num + 1):
                    for i in range(num1):
                        print('*', end='')
                    print()
                    num1 += 1
            else:
                num1 = - + num
                for i in range(num1, 0):
                    for j in range(-i):
                        print('*', end='')
                    print()
        else:
            print('You have chosen the wrong pattern style!')
    n = input('Do you want to continue [y / n] Default[n]:- ')
    if n == 'n' or n == '':
        print('I hope you like this programS!')