sen1 = 'Python is Awesome'
senrev = []
sensplit = sen1.split()
for i in range(len(sensplit)):
    senlist = list(sensplit[i])
    j = 0
    senrev.append(' ')
    while(j < len(senlist)):
        senrev.append(senlist[len(senlist)-j-1])
        j = j+1
senrev = ''.join(senrev)
print(senrev.strip())



