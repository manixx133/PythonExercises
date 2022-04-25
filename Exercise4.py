sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
rep_list = []
for i in sample_list:
    counter = 0
    for j in sample_list:
        if(i==j):
            counter=counter+1
            if (counter > 1):
                rep_list.append(i)
                sample_list.remove(i)
print('Repeating Elements are',rep_list)
