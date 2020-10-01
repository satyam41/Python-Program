# function of average

def AVG(x):
    sum1 = 0
    avg = 0
    for i in x:
        sum1 = sum1+i
        avg = sum1/len(x)
    return avg