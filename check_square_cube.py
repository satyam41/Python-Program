# Check if the Square root of the First number is Equal to the Cube root of the Second number
def prefect_cube(x):
    cube = 0
    for i in range(x+1):
        cube = i**3
        if cube == x:
            return True
        elif cube > x:
            return False

def prefect_square(y):
    sqr = 0
    for i in range(y+1):
        sqr = i**2
        if sqr == y:
            return True
        elif sqr > y:
            return False

def check_squre_cube(a,b):
    if prefect_square(a) == prefect_cube(b):
        return True
    else:
        return False
check_squre_cube(36,216)