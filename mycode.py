def power(x, y): 
    """Multiplies value x by itself y number of times.

    Args:
        x (num): any numeric object
        y (num): any positive numeric integer
    """
    if y <= 0:
        raise ValueError("y cannot be a negative number")
    
    v = x ** y # v is return value

    return(v) # return our calculation

def list_maker(y, z):
    rv = [v for v in range(y, z)] # rv = return value
    return(rv)

def avg_diff(x, y, z):
    s = sum([x, y, z]) # s = sum
    a = s / 3 # average
    rv = x - a # rv = return value
    return(rv)

def dict_grouping(x, y, z):
    d = {} # dictionary
    for i in range(x):
        d[i] = [list_maker(y, z), avg_diff(i, y, z)]
    return(d)