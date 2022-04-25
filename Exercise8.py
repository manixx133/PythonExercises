import time

def timer(funct):
    start_time = time.time()*1000
    funct()
    end_time = time.time()*1000
    print('Elapsed time in milli seconds:',(end_time - start_time))

@timer
def main_fun():
    result = []
    array = range(1, 100000)
    for number in array:
        result.append(number * number * number)
    return
