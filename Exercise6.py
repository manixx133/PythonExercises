count1 = input('Please give a number ')
count1 = int(count1)
count2 = 1
while(count1 > 0):
    rep = 1
    while(rep <= count1):
        print(count2,end =' ')
        rep = rep+1
    count1 = count1-1
    count2 = count2+1
    print('\n')