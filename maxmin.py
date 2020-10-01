# function of maximum 

def MAX(x):
    big = x[0]
    j = 0
    for i in x:
        if (x[j]>=big):
            big=x[j]
            j=j+1
        else:
            j=j+1
    return big

# function of minimum

def MIN(x):
    small = x[0]
    j = 0
    for i in x:
        if (x[j]<=small):
            small=x[j]
            j=j+1
        else:
            j=j+1
    return small 
