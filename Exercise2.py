sen1 = 'Python is Awesome'.lower()
senrev = []
sensplit = sen1.split()
for i in range(len(sensplit)):
    senlist = list(sensplit[i])
    j = 0
    senrev.append(' ')
    while(j < len(senlist)):
        if (j==0 and i!=1):
            x = senlist[len(senlist) - j - 1].upper()
            senrev.append(x)
        else:
            senrev.append(senlist[len(senlist)-j-1])
        j = j+1
senrev = ''.join(senrev)
print(senrev.strip())



