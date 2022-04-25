number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n=len(number_list)
m=0
print(number_list)
print('ID for List befor change',id(number_list))
while n!=m:
    if (number_list[m] < 50):
        number_list.remove(number_list[m])
        m=m-1
        n=n-1
    m=m+1
print(number_list)
print('ID for List befor change',id(number_list))